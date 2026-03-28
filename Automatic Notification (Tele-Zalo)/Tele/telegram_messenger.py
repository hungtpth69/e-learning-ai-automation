import requests
import csv
import time
import os

# ==============================================================
# 🎯 KHU VỰC CẤU HÌNH CỦA ỨNG DỤNG TELEGRAM
# ==============================================================
# Nạp Token từ file cấu hình tĩnh
TELEGRAM_BOT_TOKEN = ""
if os.path.exists("telegram_token.txt"):
    with open("telegram_token.txt", "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                if k.strip() == "TELEGRAM_BOT_TOKEN":
                    TELEGRAM_BOT_TOKEN = v.strip('"\' ')

# FILE DỮ LIỆU ĐẦU VÀO
FILE_CSV_DATA = "contact_list.csv"
# ==============================================================

def gui_tin_nhan_telegram(chat_id, noi_dung):
    """
    Hệ thống gọi API Telegram ẩn danh (Không có giao diện UI).
    Tốc độ cực cao do giao tiếp trực tiếp với máy chủ HTTP.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": str(chat_id).strip(),
        "text": noi_dung
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Lỗi mạng/Kết nối: {e}")
        return False

def main():
    print("==================================================")
    print("🚀 [ỨNG DỤNG 1] TELEGRAM API MESSENGER KHỞI ĐỘNG 🚀")
    print("==================================================\n")
    print("⏳ Đang tải dữ liệu từ bộ nhớ File (CSV)...")
    time.sleep(1) 
    
    danh_sach = []
    
    try:
        with open(FILE_CSV_DATA, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                danh_sach.append(row)
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file `{FILE_CSV_DATA}`.")
        return

    print(f"✅ Đã tải thành công {len(danh_sach)} liên hệ.\n")
    print("⚡ BẮT ĐẦU CHẠY CHIẾN DỊCH GỬI API NGẦM...\n")
    
    for contact in danh_sach:
        ten = contact.get('Ho_Ten', 'Bạn')
        chat_id = contact.get('Chat_ID', '')
        noi_dung = contact.get('Noi_Dung_Tuy_Chinh', '')
        
        if not chat_id:
            continue
            
        tin_nhan = f"👋 Xin chào {ten},\n\n{noi_dung}\n\n(Hệ thống tự động Tele-Bot)"
        
        thanh_cong = gui_tin_nhan_telegram(chat_id, tin_nhan)
        
        if thanh_cong:
            print(f"  [+] Đã gửi thành công (API Status 200) ➞ {ten} | ID: {chat_id}")
        else:
            print(f"  [-] Lỗi kết nối API ➞ {ten} (Yêu cầu kiểm tra ID & Token)")
        
        time.sleep(0.5) 
            
    print("\n🎉 HOÀN THÀNH ỨNG DỤNG 1! Toàn bộ yêu cầu định tuyến đã gửi xong.")
    print("==================================================")

if __name__ == "__main__":
    main()
