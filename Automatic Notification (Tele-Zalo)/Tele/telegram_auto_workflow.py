import requests
import csv
import time
import os

# ==============================================================
# 🎯 KHU VỰC CẤU HÌNH TOKEN
# ==============================================================
TELEGRAM_BOT_TOKEN = ""
if os.path.exists("telegram_token.txt"):
    with open("telegram_token.txt", "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                if k.strip() == "TELEGRAM_BOT_TOKEN":
                    TELEGRAM_BOT_TOKEN = v.strip('"\' ')
        
FILE_CSV_DATA = "contact_list.csv"

# Tin nhắn mặc định dành cho những người mới vừa nhắn tin cho Bot (Được tự động thêm vào CSV)
DEFAULT_MESSAGE = "Hệ thống đã tự động nhận diện ID của bạn và thêm vào Danh bạ thành công!"
# ==============================================================

def fetch_and_update_csv():
    print("==================================================")
    print("🔍 BƯỚC 1: TỰ ĐỘNG QUÉT SERVER & CẬP NHẬT DANH BẠ 🔍")
    print("==================================================\n")
    
    # 1.1 Đọc danh bạ hiện tại để tránh thêm trùng lặp người cũ
    existing_ids = set()
    if os.path.exists(FILE_CSV_DATA):
        with open(FILE_CSV_DATA, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_ids.add(str(row.get('Chat_ID', '')).strip())
    
    # 1.2 Gọi API lấy toàn bộ tin nhắn tương tác mới nhất
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    try:
        response = requests.get(url)
        data = response.json()
        
        if not data.get("ok"):
            print("❌ Lỗi API khi quét Server: Token có thể không hợp lệ.")
            return False
            
        messages = data.get("result", [])
        new_users_added = 0
        
        # 1.3 Ghi (Append) data người dùng mới vào thẳng CSV
        mode = 'a' if os.path.exists(FILE_CSV_DATA) else 'w'
        with open(FILE_CSV_DATA, mode=mode, encoding='utf-8-sig', newline='') as f:
            fieldnames = ['Ho_Ten', 'Chat_ID', 'So_Dien_Thoai', 'Noi_Dung_Tuy_Chinh']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if mode == 'w':
                writer.writeheader()
                
            for msg in messages:
                if "message" in msg and "from" in msg["message"]:
                    user = msg["message"]["from"]
                    chat_id = str(user.get("id"))
                    
                    if chat_id not in existing_ids:
                        first_name = user.get("first_name", "")
                        last_name = user.get("last_name", "")
                        full_name = f"{first_name} {last_name}".strip()
                        if not full_name:
                            full_name = "Khách hàng ẩn danh"
                            
                        # Thêm thẳng vào file Excel/CSV
                        writer.writerow({
                            'Ho_Ten': full_name,
                            'Chat_ID': chat_id,
                            'So_Dien_Thoai': '', 
                            'Noi_Dung_Tuy_Chinh': DEFAULT_MESSAGE
                        })
                        existing_ids.add(chat_id)
                        new_users_added += 1
                        print(f"  [+] Tự động thu thập & cập nhật data: {full_name} (ID: {chat_id})")
        
        if new_users_added == 0:
            print("  [-] Không phát hiện người dùng mới nào (Danh bạ đã đầy đủ).")
        else:
            print(f"✅ Đã thêm thành công {new_users_added} liên hệ mới vào Data CSV.")
        
        return True
    
    except Exception as e:
        print(f"❌ Lỗi quét server: {e}")
        return False

def send_telegram_messages():
    print("\n==================================================")
    print("🚀 BƯỚC 2: TỰ ĐỘNG ĐỌC DANH BẠ & GỬI TIN NHẮN 🚀")
    print("==================================================\n")
    
    danh_sach = []
    try:
        with open(FILE_CSV_DATA, mode='r', encoding='utf-8-sig') as f: # UTF-8-sig chống lỗi font Tiếng Việt
            reader = csv.DictReader(f)
            for row in reader:
                danh_sach.append(row)
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {FILE_CSV_DATA}.")
        return

    if len(danh_sach) == 0:
        print("📭 Danh bạ trống rỗng. Không có tin nhắn nào được gửi.")
        return

    print(f"✅ Bắt đầu phân phối tin nhắn cho {len(danh_sach)} liên hệ...\n")
    
    for contact in danh_sach:
        ten = contact.get('Ho_Ten', 'Bạn')
        chat_id = contact.get('Chat_ID', '')
        noi_dung = contact.get('Noi_Dung_Tuy_Chinh', '')
        
        if not chat_id:
            continue
            
        tin_nhan = f"👋 Xin chào {ten},\n\n{noi_dung}\n\n(Hệ thống gửi tự động từ Python)"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        
        try:
            response = requests.post(url, json={"chat_id": chat_id, "text": tin_nhan})
            if response.status_code == 200:
                print(f"  [➔] Đã gửi thành công ➞ {ten} | ID: {chat_id}")
            else:
                print(f"  [✖] Lỗi API từ chối ➞ {ten} (Có thể Chat_ID sai hoặc User chặn Bot)")
        except Exception as e:
            print(f"  [✖] Lỗi rớt mạng ➞ {ten}: {e}")
        
        time.sleep(0.5) 

    print("\n🎉 HOÀN THÀNH TOÀN BỘ WORKFLOW! Tự động lấy data và tự động Marketing.")

if __name__ == "__main__":
    success = fetch_and_update_csv()
    if success:
        time.sleep(3) # Nghỉ xíu cho người xem theo dõi kịp tiến trình hiển thị trên console
        send_telegram_messages()
