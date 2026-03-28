import os
import csv
import time
import asyncio
from telethon import TelegramClient

# =======================================================
# 🎯 CẤU HÌNH API ID & HASH TỪ my.telegram.org
# =======================================================
API_ID = ""
API_HASH = ""

config_path = "telethon_config.txt"
if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                if k.strip() == "API_ID":
                    API_ID = v.strip('"\' ')
                elif k.strip() == "API_HASH":
                    API_HASH = v.strip('"\' ')

FILE_CSV_DATA = "userbot_contact_list.csv"

async def main():
    print("==================================================")
    print("🚀 TELEGRAM USERBOT (TÀI KHOẢN CÁ NHÂN) KHỞI ĐỘNG 🚀")
    print("==================================================\n")
    
    if not API_ID or not API_HASH:
        print("❌ Chưa cấu hình API_ID và API_HASH trong file telethon_config.txt")
        return

    print("⚠️ LƯU Ý BẢO MẬT: Trong lần chạy ĐẦU TIÊN, hệ thống console sẽ yêu cầu bạn nhập SĐT và Mã OTP gửi về Telegram.")
    print("Tuyệt đối KHÔNG chia sẻ file dạng .session sinh ra sau đó cho bất kỳ ai!\n")
    
    # Khởi tạo Client mô phỏng ứng dụng Telegram
    client = TelegramClient('tai_khoan_cua_toi', int(API_ID), API_HASH)
    
    # Kết nối lên máy chủ MTProto
    await client.start()
    print("✅ Mạng lưới khai thông! Đăng nhập Thành Công bằng Tài Khoản Cá Nhân!\n")
    
    danh_sach = []
    if os.path.exists(FILE_CSV_DATA):
        with open(FILE_CSV_DATA, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                danh_sach.append(row)
                
    if not danh_sach:
        print(f"📭 Danh bạ trống rỗng. Hãy điền data vào {FILE_CSV_DATA}.")
        return
        
    print(f"⚡ BẮT ĐẦU GỬI ĐỒNG LOẠT TIN NHẮN TỚI {len(danh_sach)} LIÊN HỆ...\n")
    
    for contact in danh_sach:
        ten = contact.get('Ho_Ten', 'Bạn')
        target = contact.get('Username_hoac_Sdt', '')
        noi_dung = contact.get('Noi_Dung_Tuy_Chinh', '')
        
        if not target:
            continue
            
        tin_nhan = f"👋 Xin chào {ten},\n\n{noi_dung}\n\n(Lưu ý: Tin nhắn được phần mềm tự động phát đi từ nick chính chủ của tôi!)"
        
        try:
            # Telethon hỗ trợ gửi tin cho cả Username (@username) hoặc Số điện thoại có mã quốc gia (+84)
            await client.send_message(target, tin_nhan)
            print(f"  [+] Đã gửi đi thành công ➞ {ten} | Tới định danh: {target}")
        except Exception as e:
            print(f"  [-] Lỗi đường truyền tới ➞ {ten} ({target}): {e}")
        
        # [CẢNH BÁO MẠNG]: Telethon gửi bằng tài khoản thật nên bắt buộc phải ngâm delay rất lâu để không bị mạng lưới AI Telegram khóa nick (Khuyến cáo 5-10s)
        time.sleep(5) 
        
    print("\n🎉 HOÀN THÀNH CHIẾN DỊCH BẰNG TÀI KHOẢN CÁ NHÂN!")
    print("==================================================")
    
    # Ngắt liên kết an toàn
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
