import smtplib
import csv
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# ==============================================================
# 🎯 CẤU HÌNH GMAIL SMTP
# ==============================================================
# Lấy Password dùng chung từ hệ thống gốc (Thư mục cha)
config = {}
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "email_config.txt")
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                config[k.strip()] = v.strip('"\' ')

GMAIL_ADDRESS = config.get("GMAIL_ADDRESS", "")
GMAIL_APP_PASSWORD = config.get("GMAIL_APP_PASSWORD", "")

FILE_INPUT_CSV = "offer_list.csv"
FILE_LOG_CSV = "demo_sent_log.csv"
FILE_HTML_TEMPLATE = "offer_template.html"
FILE_ATTACHMENT = "Thu_Tuc_Nhan_Viec.txt"

# ==============================================================
# 🧩 CÁC SKILL CỦA HỆ THỐNG AGENT (DEMO ĐÍNH KÈM FILE)
# ==============================================================

def skill_read_data():
    """Skill 1: Tìm đọc danh sách trúng tuyển"""
    print("🤖 [Agent] Thu thập Data ứng viên...")
    danh_sach = []
    if os.path.exists(FILE_INPUT_CSV):
        with open(FILE_INPUT_CSV, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                danh_sach.append(row)
    return danh_sach

def skill_generate_html_email(ho_ten, vi_tri, muc_luong):
    """Skill 2: Ép Plastic HTML ghép Tên, Vị trí, Lương"""
    if not os.path.exists(FILE_HTML_TEMPLATE):
        return f"<h3>Thư Mời Nhận Việc</h3><br>Mời {ho_ten} nhận vị trí {vi_tri} với lương {muc_luong}."
    with open(FILE_HTML_TEMPLATE, mode='r', encoding='utf-8') as f:
        html_content = f.read()
    html_content = html_content.replace("{{HO_TEN}}", ho_ten)
    html_content = html_content.replace("{{VI_TRI}}", vi_tri)
    html_content = html_content.replace("{{MUC_LUONG}}", muc_luong)
    return html_content

def skill_notify_smtp_with_attachment(email_nhan, ho_ten, vi_tri, html_content):
    """Skill 3: Đẩy thư kèm File lên Cổng Viễn Thông TCP 587"""
    try:
        msg = MIMEMultipart()
        msg['From'] = f"Phòng Nhân Sự Antigravity <{GMAIL_ADDRESS}>"
        msg['To'] = email_nhan
        msg['Subject'] = f"🎊 THƯ MỜI NHẬN VIỆC (OFFER LETTER) - {ho_ten} - {vi_tri}"
        
        # 1. Nhét Giấy Ruột (Nội dung HTML)
        msg.attach(MIMEText(html_content, 'html'))

        # 2. Xử lý Đính kèm (Tệp Document/PDF)
        if os.path.exists(FILE_ATTACHMENT):
            with open(FILE_ATTACHMENT, "rb") as attachment:
                # Đóng gói MIME Base64 hệ nhị phân
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename= {FILE_ATTACHMENT}")
            msg.attach(part) # Gắn chặt File vào Email

        # 3. Kích hoạt SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        
        server.send_message(msg)
        server.quit()
        return {"error": 0, "message": "Success"}
    except Exception as e:
        return {"error": -1, "message": str(e)}

def skill_log_result(ho_ten, email, trang_thai):
    """Skill 4: Thư Ký Xuất Báo Cáo"""
    mode = 'a' if os.path.exists(FILE_LOG_CSV) else 'w'
    with open(FILE_LOG_CSV, mode=mode, encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        if mode == 'w':
            writer.writerow(["Thoi_Gian", "Ho_Ten", "Email", "Ket_Qua_Trang_Thai"])
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), ho_ten, email, trang_thai])

def main():
    print("======================================================")
    print("🛸 DEMO AGENT WORKFLOW: GỬI OFFER LETTER KÈM TỆP (ATTACHMENTS) 🛸")
    print("======================================================\n")
    
    danh_sach = skill_read_data()
    if not danh_sach:
        print("❌ Data rỗng!")
        return
        
    print(f"\n🚀 ĐÃ TÌM THẤY {len(danh_sach)} ỨNG VIÊN. BẮT ĐẦU VÒNG LẶP GỬI THƯ...\n")

    for ns in danh_sach:
        ten = ns.get('Ho_Ten', 'Bạn')
        email = ns.get('Email', '')
        vt = ns.get('Vi_Tri', '')
        luong = ns.get('Muc_Luong', '')

        if not email: continue
            
        print("-" * 55)
        # Sinh Template Đóng Khung
        noi_dung_html = skill_generate_html_email(ten, vt, luong)
        
        # Bóp Cò Gửi có đính kèm File
        print(f"📨 [Agent] Đang kẹp chung file Tài Liệu và đẩy SMTP tới: {email}...")
        ket_qua = skill_notify_smtp_with_attachment(email, ten, vt, noi_dung_html)
        
        if ket_qua.get("error") == 0:
            print(f"  [➔] THÀNH CÔNG ➞ Thư Offer đã đến hộp Tới của {ten}.")
            trang_thai_log = "Thành Công"
        else:
            msg = ket_qua.get("message")
            print(f"  [✖] THẤT BẠI ➞ SMTP từ chối người dùng {email}: {msg[:50]}...")
            trang_thai_log = f"Lỗi: {msg}"

        skill_log_result(ten, email, trang_thai_log)
        time.sleep(1.5) # Chống Spam bóp rate của Google

    print("-" * 55)
    print("🎉 HOÀN THÀNH TOÀN BỘ 10 CHIẾN DỊCH DEMO!")
    print("👉 Hãy mở [THƯ ĐÃ GỬI] của bạn để xem 10 Cái Email trông lộng lẫy và hoàn hảo như thế nào nhé.")

if __name__ == "__main__":
    main()
