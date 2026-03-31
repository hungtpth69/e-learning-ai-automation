"""
Zalo Web DOM Automation (UserBot) - Chế độ ĐỌC TIN NHẮN
Sử dụng thư viện Playwright để tìm số điện thoại và cào nội dung tin nhắn chat gần nhất.
"""

from playwright.sync_api import sync_playwright
import time
import csv
import os

def read_zalo_messages(csv_file='read_list.csv', num_messages=5):
    print("🚀 Bắt đầu khởi chạy Zalo UserBot (Chế độ ĐỌC TIN NHẮN)...")
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
        
        print("⏳ Đang chờ nạp Cookie đăng nhập...")
        try:
            page.wait_for_selector('#contact-search-input', timeout=60000)
            print("✅ Đăng nhập Zalo Web thành công!")
        except Exception:
            print("❌ Quá thời gian hoặc lỗi cấu trúc Zalo: Không tìm thấy thanh tìm kiếm.")
            browser.close()
            return
            
        print(f"📂 Đang lấy tin nhắn cho các liên hệ trong {csv_file}...\n")
        
        try:
            with open(csv_file, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    phone = row['Phone Number'].strip()
                    name = row['Name'].strip()
                    
                    print(f"\n-> Đang mở đoạn chat của: {name} ({phone})")
                    
                    search_input = page.locator('#contact-search-input')
                    search_input.click()
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    time.sleep(1)
                    
                    search_input.fill(phone)
                    time.sleep(3) 
                    
                    page.keyboard.press('Enter')
                    time.sleep(3) 
                    
                    print("   🤖 Đang sử dụng Agent quét cấu trúc DOM để trích xuất tin nhắn...")
                    
                    try:
                        message_elements = page.locator('span.text, div.text-content, div.card--text, div[id^="msg-"]')
                        count = message_elements.count()
                        if count == 0:
                            try:
                                text_fallback = page.locator('.message-view__blur__chat-content, #messageViewContainer, .chat-message-list').first.inner_text()
                                print(f"   [Nội Dung Khung Chat]:\n   {text_fallback[-500:]}")
                            except:
                                print("   [🔴] Không thể lấy tin nhắn từ người này.")
                        else:
                            start_idx = max(0, count - num_messages)
                            print(f"   [🟢] Lấy ra {min(num_messages, count)} nội dung mới nhất:")
                            for i in range(start_idx, count):
                                msg_text = message_elements.nth(i).inner_text().strip()
                                if msg_text:
                                    msg_short = msg_text.replace('\n', ' ')
                                    if len(msg_short) > 150: 
                                        msg_short = msg_short[:150] + '...'
                                    print(f"      - {msg_short}")
                                    
                    except Exception as e:
                        print(f"   [🔴] Lỗi kỹ thuật khi phân tích DOM: {e}")
                    
                    time.sleep(2)
                    
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file {csv_file}.")
            
        print("\n🎉 Đã hoàn thành luồng đọc tin nhắn UserBot!")
        browser.close()

if __name__ == '__main__':
    read_zalo_messages()
