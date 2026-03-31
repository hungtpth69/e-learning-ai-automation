import os
import time
from playwright.sync_api import sync_playwright

def read_recent_zalo_messages(max_chats=10):
    print("🚀 Bắt đầu khởi chạy Zalo UserBot (Chế độ ĐỌC TIN NHẮN GẦN ĐÂY - Bỏ qua Số Điện Thoại)...")
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
            # Chờ danh sách cuộc trò chuyện xuất hiện
            page.wait_for_selector('.msg-item', timeout=60000)
            print("✅ Đăng nhập Zalo Web thành công!")
        except Exception:
            print("❌ Quá thời gian hoặc lỗi cấu trúc Zalo: Không tìm thấy danh sách tin nhắn.")
            browser.close()
            return
            
        print(f"📂 Đang duyệt qua {max_chats} cuộc trò chuyện gần nhất...\n")
        
        # Tìm tất cả các khung chat mở gần đây ở cột trái
        msg_items = page.locator('.msg-item').all()
        count = len(msg_items)
        
        if count == 0:
            print("   [🔴] Không tìm thấy cuộc trò chuyện nào trong danh sách gần đây.")
            browser.close()
            return
            
        print(f"   Tìm thấy {count} cuộc trò chuyện. Lấy tối đa {max_chats}...")
        
        extracted_data = {}
        limit = min(count, max_chats)
        
        for i in range(limit):
            msg_item = msg_items[i]
            
            try:
                # Trích xuất tên của đoạn chat để in ra log
                name_el = msg_item.locator('.conv-item-title__name')
                chat_name = name_el.inner_text().strip() if name_el.count() > 0 else f"Conversation {i+1}"
                
                print(f"\n=====================================")
                print(f"-> Đang xem đoạn chat: {chat_name}")
                
                # Bấm vào cuộc trò chuyện
                msg_item.click()
                time.sleep(2)
                
                # Kiểm tra nút đồng bộ
                sync_btn = page.locator('text=Đồng bộ ngay')
                if sync_btn.count() > 0 and sync_btn.first.is_visible():
                    print("   [⚠️] TÀI KHOẢN CHƯA ĐỒNG BỘ. Cố gắng tự động bấm nút 'Đồng bộ ngay'...")
                    
                    try:
                        sync_btn.first.click()
                        print("   [🔔] Đã bấm Đồng bộ! 👉 VUI LÒNG MỞ APP ZALO TRÊN ĐIỆN THOẠI VÀ CHỌN 'ĐỒNG Ý ĐỒNG BỘ'...")
                        
                        # Chờ nút đồng bộ biến mất (nghĩa là đã đồng bộ xong) tối đa 60 giây
                        sync_btn.first.wait_for(state='hidden', timeout=60000)
                        print("   [✅] Thiết bị đã đồng bộ thành công! Đang tải lại tin nhắn...")
                        time.sleep(3) # Cho DOM render xong tin nhắn cũ
                    except Exception:
                        print("   [🔴] Quá 60 giây vẫn chưa xác nhận qua điện thoại. Sẽ bỏ qua đọc nội dung này.")
                        extracted_data[chat_name] = ["CHƯA ĐỒNG BỘ (Timeout)"]
                        continue
                
                # Cuộn lên để tải tin nhắn cũ
                page.mouse.wheel(0, -2000)
                time.sleep(2)
                
                # Đọc inner_text của container hiển thị tin nhắn
                chat_text = page.evaluate('() => document.querySelector("#messageViewContainer, #messageViewScroll, .message-view__scroll__inner")?.innerText || ""')
                
                if chat_text:
                    lines = [line.strip() for line in chat_text.split('\n') if line.strip()]
                    
                    # Lọc tin nhắn trong 24h: Tìm vị trí 'Hôm nay' hoặc 'Hôm qua'
                    start_idx = 0
                    for k in reversed(range(len(lines))):
                        if lines[k] in ['Hôm nay', 'Hôm qua']:
                            start_idx = k
                            break
                    
                    recent_lines = lines[start_idx:]
                    if not recent_lines:
                        recent_lines = lines[-20:] # Fallback nếu không tìm thấy nhãn
                        
                    print(f"   [🟢] Nội dung 24h qua ({len(recent_lines)} dòng):")
                    for line in recent_lines:
                        print(f"      | {line}")
                        
                    extracted_data[chat_name] = recent_lines
                else:
                    print("   [🔴] Khung chat trống hoặc không thể lấy text.")
                    
            except Exception as e:
                print(f"   [🔴] Lỗi khi xử lý đoạn chat thứ {i+1}: {e}")
                
        print("\n🎉 Đã hoàn thành duyệt danh sách chat!")
        browser.close()

if __name__ == '__main__':
    read_recent_zalo_messages(max_chats=10)
