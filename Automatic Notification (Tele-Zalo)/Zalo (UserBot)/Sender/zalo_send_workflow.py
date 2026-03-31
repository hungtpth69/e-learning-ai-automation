"""
Zalo Web DOM Automation (UserBot) Workflow
Sử dụng thư viện Playwright để giả lập thao tác duyệt web trên Zalo Web (chat.zalo.me).
"""

from playwright.sync_api import sync_playwright
import time
import csv
import os
import random

def send_zalo_messages(csv_file='send_list.csv'):
    print("🚀 Bắt đầu khởi chạy Zalo UserBot với Playwright (Chế độ GỬI TIN)...")
    with sync_playwright() as p:
        # Đường dẫn lưu Cookie phiên đăng nhập Zalo (Chỉ chung 1 thư mục ở cấp cha cho cả 2 Use Case)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        user_data_dir = os.path.join(base_dir, 'zalo_user_data_session')
        
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            no_viewport=True 
        )
        
        page = browser.pages[0]
        print("🌐 Đang truy cập Zalo Web (chat.zalo.me)...")
        page.goto('https://chat.zalo.me/')
        
        print("⏳ Vui lòng quét mã QR đăng nhập nếu đây là lần đầu...")
        try:
            page.wait_for_selector('#contact-search-input', timeout=60000)
            print("✅ Đăng nhập Zalo Web thành công!")
        except Exception:
            print("❌ Quá thời gian chờ đăng nhập (60 giây) hoặc không tìm thấy thanh tìm kiếm. Lỗi.")
            browser.close()
            return
            
        print(f"📂 Đang đọc danh sách từ file {csv_file} và gửi tin nhắn...")
        
        try:
            with open(csv_file, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    phone = row['Phone Number'].strip()
                    name = row['Name'].strip()
                    message_template = row['Message Template']
                    
                    final_message = message_template.replace('{name}', name)
                    print(f"\n-> Đang xử lý liên hệ: {name} ({phone})")
                    
                    search_input = page.locator('#contact-search-input')
                    search_input.click()
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    time.sleep(1)
                    
                    search_input.fill(phone)
                    time.sleep(3) 
                    
                    page.keyboard.press('Enter')
                    time.sleep(2) 
                    
                    try:
                        chat_input = page.locator('#richInput') 
                        chat_input.wait_for(timeout=5000)
                        chat_input.click()
                        
                        page.keyboard.type(final_message, delay=random.randint(20, 50)) 
                        time.sleep(1)
                        page.keyboard.press('Enter')
                        print(f"   🟢 [Thành công] Đã gửi tin nhắn cho {name}.")
                    except Exception:
                        print(f"   🔴 [Thất bại] Lỗi khi gửi cho {phone}: Không tìm thấy khung chat hoặc bị chặn.")
                    
                    delay_time = random.randint(5, 10)
                    print(f"   ⏳ Nghỉ {delay_time} giây trước khi gửi tiếp...")
                    time.sleep(delay_time)
                    
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file {csv_file}.")
            
        print("\n🎉 Đã hoàn tất luồng nhắn tin tự động Zalo UserBot!")
        browser.close()

if __name__ == '__main__':
    send_zalo_messages()
