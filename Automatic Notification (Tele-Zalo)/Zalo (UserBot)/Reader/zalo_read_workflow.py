from playwright.sync_api import sync_playwright
import time
import csv
import os
import re

def read_zalo_messages(csv_file='read_list.csv', num_messages=10):
    print("🚀 Bắt đầu khởi chạy Zalo UserBot (Chế độ ĐỌC TIN NHẮN 24H)...")
    with sync_playwright() as p:
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
        
        extracted_data = {}

        try:
            with open(csv_file, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    phone = row['Phone Number'].strip()
                    name = row['Name'].strip()
                    
                    print(f"\n=====================================")
                    print(f"-> Đang mở đoạn chat của: {name} ({phone})")
                    
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
                    
                    # Kiểm tra nút đồng bộ
                    sync_btn = page.locator('text=Đồng bộ ngay')
                    if sync_btn.count() > 0:
                        print("   [⚠️] TÀI KHOẢN CHƯA ĐỒNG BỘ: Zalo đang yêu cầu 'Đồng bộ ngay'. Không thể đọc lịch sử trò chuyện cũ trên thiết bị này.")
                    
                    try:
                        # Cuộn lên một chút để load tin nhắn cũ nếu cần
                        page.mouse.wheel(0, -2000)
                        time.sleep(2)
                        
                        # Lấy innerText của khung chat, nó thường chứa cả Ngày tháng và Giờ
                        chat_text = page.evaluate('() => document.querySelector("#messageViewContainer, #messageViewScroll, .message-view__scroll__inner")?.innerText || ""')
                        
                        if chat_text:
                            # Tách thành mảng các dòng và in ra
                            lines = [line.strip() for line in chat_text.split('\n') if line.strip()]
                            print(f"   [🟢] Raw chat content (latest {num_messages*2} lines):")
                            for line in lines[-num_messages*2:]:
                                print(f"      | {line}")
                            
                            extracted_data[name] = lines
                        else:
                            print("   [🔴] Khung chat trống hoặc không thể lấy text.")
                                    
                    except Exception as e:
                        print(f"   [🔴] Lỗi kỹ thuật khi phân tích DOM: {e}")
                    
                    time.sleep(2)
                    
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file {csv_file}.")
            
        print("\n🎉 Đã hoàn thành luồng đọc tin nhắn UserBot!")
        browser.close()

if __name__ == '__main__':
    read_zalo_messages()
