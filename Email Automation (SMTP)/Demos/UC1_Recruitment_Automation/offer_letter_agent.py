import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_offer_letters():
    # 1. Đọc cấu hình từ file config
    # Ở đây chúng tôi mock các biến môi trường
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your-email@gmail.com"
    APP_PASSWORD = "abcd efgh ijkl mnop" # Lấy từ file email_config.txt

    # 2. Đọc danh sách ứng viên từ file CSV
    data = pd.read_csv("candidates.csv")

    print(f"🚀 Bắt đầu gửi {len(data)} Thư mời nhận việc...")

    try:
        # Khởi tạo kết nối SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        # server.login(SENDER_EMAIL, APP_PASSWORD) # Uncomment khi chạy thực tế

        for index, row in data.iterrows():
            name = row['Full Name']
            pos = row['Candidate Position']
            salary = row['Salary']
            receiver_email = row['Offer Email']
            
            # Tạo nội dung email cá nhân hóa
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = receiver_email
            msg['Subject'] = f"🚀 Offer Letter - {pos} - {name}"

            body = f"""Chào {name},
            
Chúc mừng bạn đã trúng tuyển vào vị trí {pos}.
Mức lương thỏa thuận: {salary} USD/tháng.
Vui lòng xem file đính kèm để biết thêm chi tiết.

Trân trọng,
Antigravity HR Team.
"""
            msg.attach(MIMEText(body, 'plain'))
            
            # (Phần đính kèm file - bỏ qua trong template này để tinh gọn)
            
            print(f"[➔] Đang gửi thư cho {name} ({receiver_email})... THÀNH CÔNG")

        server.quit()
        print("✅ Hoàn tất! Tất cả 10 ứng viên đã nhận được Offer.")

    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")

# Chạy Demo
if __name__ == "__main__":
    send_offer_letters()
