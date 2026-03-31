import imaplib
import email
from email.header import decode_header
import csv
import datetime

username = "hung.tran@danishsoftware.com"
password = "tcwauavxvekxrblr"

try:
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select("INBOX")

    # Calculate date 2 days ago
    date_2_days_ago = (datetime.date.today() - datetime.timedelta(2)).strftime("%d-%b-%Y")
    status, messages = imap.search(None, f'(SINCE "{date_2_days_ago}")')

    email_ids = messages[0].split()
    subjects = []

    for e_id in email_ids:
        # Fetch only the subject header to save time and bandwidth
        res, msg_data = imap.fetch(e_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject_header = msg.get("Subject", "(Không có tiêu đề)")
                if subject_header:
                    decoded_parts = decode_header(subject_header)
                    subject_text = ""
                    for part, encoding in decoded_parts:
                        if isinstance(part, bytes):
                            try:
                                subject_text += part.decode(encoding or 'utf-8', errors='ignore')
                            except LookupError:
                                subject_text += part.decode('utf-8', errors='ignore')
                        else:
                            subject_text += part
                    subjects.append([subject_text])

    imap.logout()
    
    # Reverse to list newest first
    subjects.reverse()
    
    csv_filename = "recent_email_titles.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(["Tiêu đề Email"])
        writer.writerows(subjects)

    print(f"Lưu thành công {len(subjects)} tiêu đề email vào file {csv_filename}")
except Exception as e:
    print(f"Lỗi: {e}")
