import smtplib
import csv
import time
import os
import json
import urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==============================================================
# 🎯 CẤU HÌNH HỆ THỐNG GỬI EMAIL (Từ file email_config.txt)
# ==============================================================
config = {}
if os.path.exists("email_config.txt"):
    with open("email_config.txt", "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                config[k.strip()] = v.strip('"\' ')
# Chọn 1 trong 3 phương thức: "smtp", "resend", hoặc "sendgrid"
EMAIL_PROVIDER = config.get("EMAIL_PROVIDER", "smtp")

# 1. CẤU HÌNH GMAIL SMTP (Dùng App Password)
GMAIL_ADDRESS = config.get("GMAIL_ADDRESS", "your_email@gmail.com")
GMAIL_APP_PASSWORD = config.get("GMAIL_APP_PASSWORD", "")

# 2. CẤU HÌNH RESEND API
RESEND_API_KEY = config.get("RESEND_API_KEY", "")
RESEND_SENDER = config.get("RESEND_SENDER", "onboarding@resend.dev")

# 3. CẤU HÌNH SENDGRID API
SENDGRID_API_KEY = config.get("SENDGRID_API_KEY", "")
SENDGRID_SENDER = config.get("SENDGRID_SENDER", "marketing@yourdomain.com")

FILE_INPUT_CSV = "email_contact_list.csv"
FILE_LOG_CSV = "email_sent_log.csv"
FILE_HTML_TEMPLATE = "email_template.html"

# ==============================================================
# 🧩 CÁC SKILL CỦA HỆ THỐNG AGENT (EMAIL AUTOMATION)
# ==============================================================

def skill_read_data():
    """Agent Skill 1: Thu thập bộ Dữ liệu Cốt Lõi đa năng"""
    print("🤖 [Agent] Kích hoạt skill_read_data()...")
    danh_sach = []
    if not os.path.exists(FILE_INPUT_CSV):
        print(f"❌ Không tìm thấy file `{FILE_INPUT_CSV}`.")
        return danh_sach
        
    with open(FILE_INPUT_CSV, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            danh_sach.append(row)
    print(f"✅ [Agent] Đã tải thành công {len(danh_sach)} liên hệ Email.")
    return danh_sach

def skill_generate_html_email(tieu_de, noi_dung_tuy_chinh):
    """Agent Skill 2: AI trộn nội dung Custom Content vào Form HTML tĩnh"""
    print(f"🧠 [Agent] Lắp ráp (Generate) khung HTML động...")
    time.sleep(0.5) 
    
    if not os.path.exists(FILE_HTML_TEMPLATE):
        return f"<h3>{tieu_de}</h3><br>{noi_dung_tuy_chinh}"

    with open(FILE_HTML_TEMPLATE, mode='r', encoding='utf-8') as f:
        html_content = f.read()

    # Nội dung Customize được nhét linh hoạt vào lõi HTML
    html_content = html_content.replace("{{TIEU_DE}}", tieu_de)
    html_content = html_content.replace("{{NOI_DUNG}}", noi_dung_tuy_chinh)

    return html_content

def skill_notify_smtp(email_nhan, tieu_de_email, html_content):
    """Agent Skill 3.1: Đẩy thư qua Cổng Viễn Thông TCP/IP của Google SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = f"Hệ Thống Phân Phối AI <{GMAIL_ADDRESS}>"
        msg['To'] = email_nhan
        msg['Subject'] = f"🚀 Thông báo tự động: {tieu_de_email}"
        
        msg.attach(MIMEText(html_content, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        
        server.send_message(msg)
        server.quit()
        return {"error": 0, "message": "Success"}
    except Exception as e:
        return {"error": -1, "message": str(e)}

def skill_notify_resend(email_nhan, tieu_de_email, html_content):
    """Agent Skill 3.2: Gửi thư bằng HTTP REST API của Resend"""
    try:
        url = "https://api.resend.com/emails"
        headers = {
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "from": f"Hệ Thống AI <{RESEND_SENDER}>",
            "to": [email_nhan],
            "subject": f"🚀 Thông báo tự động: {tieu_de_email}",
            "html": html_content
        }
        
        # Sử dụng urllib (thư viện gốc của Python, không cần pip install)
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return {"error": 0, "message": f"Success Resend (ID: {res_data.get('id')})"}
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'read'):
            error_msg = e.read().decode('utf-8')
        return {"error": -1, "message": f"Resend API Error: {error_msg}"}

def skill_notify_sendgrid(email_nhan, tieu_de_email, html_content):
    """Agent Skill 3.3: Gửi thư bằng HTTP REST API của SendGrid"""
    try:
        url = "https://api.sendgrid.com/v3/mail/send"
        headers = {
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "personalizations": [{"to": [{"email": email_nhan}]}],
            "from": {"email": SENDGRID_SENDER, "name": "Hệ Thống AI"},
            "subject": f"🚀 Thông báo tự động: {tieu_de_email}",
            "content": [{"type": "text/html", "value": html_content}]
        }
        
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
        with urllib.request.urlopen(req) as response:
            return {"error": 0, "message": "Success SendGrid"}
    except Exception as e:
        error_msg = str(e)
        if hasattr(e, 'read'):
            error_msg = e.read().decode('utf-8')
        return {"error": -1, "message": f"SendGrid API Error: {error_msg}"}

def skill_log_result(ho_ten, email, trang_thai):
    """Agent Skill 4: Xuất sổ cái CSV báo cáo cấp trên"""
    mode = 'a' if os.path.exists(FILE_LOG_CSV) else 'w'
    with open(FILE_LOG_CSV, mode=mode, encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        if mode == 'w':
            writer.writerow(["Thoi_Gian_Xu_Ly", "Ho_Ten", "Email", "Ket_Qua_Trang_Thai"])
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([current_time, ho_ten, email, trang_thai])

# ==============================================================
# ⚙️ HỆ ĐIỀU HÀNH AGENT (ORCHESTRATOR)
# ==============================================================
def main():
    print("======================================================")
    print("🛸 HỆ THỐNG AGENT WORKFLOW: GỬI DYNAMIC EMAIL 🛸")
    print(f"📡 Đang sử dụng phương thức: {EMAIL_PROVIDER.upper()}")
    print("======================================================\n")
    
    # Kích hoạt Skill 1
    danh_sach = skill_read_data()
    if not danh_sach:
        return
        
    print("\n🚀 BẮT ĐẦU CHUỖI XỬ LÝ WORKFLOW ĐA BƯỚC...\n")

    for ns in danh_sach:
        ten = ns.get('Ho_Ten', 'Khách hàng')
        email = ns.get('Email', '')
        tieu_de = ns.get('Tieu_De_Email', 'Thông báo quan trọng')
        noi_dung = ns.get('Noi_Dung_Tuy_Chinh', '')

        if not email or "@" not in email:
            continue
            
        print("-" * 55)
        # Kích hoạt Skill 2 (Dynamic HTML generation)
        noi_dung_html = skill_generate_html_email(tieu_de, noi_dung)
        
        print(f"📨 [Agent] Kích hoạt {EMAIL_PROVIDER.upper()} kết nối gửi thư cho: {email}...")
        
        # CHUYỂN MẠCH (SWITCH CASE) THEO PROVIDER
        if EMAIL_PROVIDER == "smtp":
            ket_qua = skill_notify_smtp(email, tieu_de, noi_dung_html)
        elif EMAIL_PROVIDER == "resend":
            ket_qua = skill_notify_resend(email, tieu_de, noi_dung_html)
        elif EMAIL_PROVIDER == "sendgrid":
            ket_qua = skill_notify_sendgrid(email, tieu_de, noi_dung_html)
        else:
            ket_qua = {"error": -1, "message": "Lỗi: PROVIDER không hợp lệ. Vui lòng kiểm tra lại cấu hình."}
        
        if ket_qua.get("error") == 0:
            print(f"  [➔] THÀNH CÔNG ➞ Kịch bản '{tieu_de}' phát đi trót lọt.")
            trang_thai_log = "Thành Công"
        else:
            msg = ket_qua.get("message")
            print(f"  [✖] THẤT BẠI ➞ Hệ thống {EMAIL_PROVIDER.upper()} từ chối: {msg[:100]}...")
            trang_thai_log = f"Lỗi: {msg}"

        # Kích hoạt Skill 4
        skill_log_result(ten, email, trang_thai_log)
        time.sleep(1) # Tránh Rate Limit

    print("-" * 55)
    print("🎉 HOÀN THÀNH TOÀN BỘ CHIẾN DỊCH EMAIL MARKETING!")
    print("👉 Hãy kiểm tra thử file Log `email_sent_log.csv` xem Thư Ký báo cáo kết quả thế nào nhé.")

if __name__ == "__main__":
    main()
