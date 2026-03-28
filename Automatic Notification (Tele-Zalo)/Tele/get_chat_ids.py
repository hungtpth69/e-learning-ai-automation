import requests
import os

# Nạp Token từ file cấu hình tĩnh
TELEGRAM_BOT_TOKEN = ""
if os.path.exists("telegram_token.txt"):
    with open("telegram_token.txt", "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                if k.strip() == "TELEGRAM_BOT_TOKEN":
                    TELEGRAM_BOT_TOKEN = v.strip('"\' ')

def get_latest_chat_ids():
    print("==================================================")
    print("🔍 TỰ ĐỘNG QUÉT CHAT ID TỪ SERVER TELEGRAM 🔍")
    print("==================================================\n")
    print("⏳ Đang lắng nghe xem có ai đang tương tác với Bot không...\n")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if not data.get("ok"):
            print("❌ Lỗi API Token: Hãy kiểm tra lại biến TELEGRAM_BOT_TOKEN có đúng không.")
            return
            
        messages = data.get("result", [])
        if len(messages) == 0:
            print("📭 Giao diện trống rỗng: Chưa có ai nhắn tin cho Bot.")
            print("👉 Hướng dẫn: Yêu cầu học viên vào tìm tên Bot, bấm /start và gửi chữ 'Hello' rồi bạn chạy lại file này.")
            return
            
        users_found = {}
        for msg in messages:
            # Lọc thông báo là Tin nhắn (message) do Người dùng gửi (from)
            if "message" in msg and "from" in msg["message"]:
                user = msg["message"]["from"]
                chat_id = user.get("id")
                first_name = user.get("first_name", "")
                last_name = user.get("last_name", "")
                # Ghép tên cho dễ nhìn
                full_name = f"{first_name} {last_name}".strip()
                
                # Lưu vào Dictionary để khử trùng lặp (1 người nhắn nhiều lần vẫn chỉ sinh ra 1 ID)
                users_found[chat_id] = full_name
                
        print("✅ ĐÃ TICK XUẤT THÀNH CÔNG DANH SÁCH CHAT ID TƯƠNG TÁC:")
        print("-" * 50)
        for cid, name in users_found.items():
            print(f"👤 Học viên: {name} ➞ Chat ID: {cid}")
        print("-" * 50)
        print("\n👉 Hãy copy các dòng Số Chat ID này và dán vào cột Chat_ID trong file contact_list.csv nhé!")
        
    except Exception as e:
        print(f"❌ Lỗi kết nối mạng: {e}")

if __name__ == "__main__":
    get_latest_chat_ids()
