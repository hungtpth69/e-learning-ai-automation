from playwright.sync_api import sync_playwright
import time
import os

def run_sync():
    print("🚀 Đang mở Zalo Web trên Chromium (Playwright) để bạn ĐỒNG BỘ DỮ LIỆU...")
    with sync_playwright() as p:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        user_data_dir = os.path.join(base_dir, 'zalo_user_data_session')
        
        # Mở profile Chromium riêng biệt mà các script tự động đang dùng
        browser = p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            viewport={'width': 1280, 'height': 800}
        )
        
        page = browser.pages[0]
        page.goto('https://chat.zalo.me/')
        
        print("✅ Trình duyệt đã mở. Hãy thao tác trên màn hình Chromium vừa hiện lên.")
        print("-" * 50)
        print("👉 HƯỚNG DẪN ĐỒNG BỘ:")
        print("1. Nếu chưa đăng nhập, hãy quét mã QR hoặc nhập mật khẩu.")
        print("2. Khi vào giao diện, tìm nút 'Đồng bộ ngay' (Sync Messages).")
        print("3. Bấm vào nút đó và mở ứng dụng Zalo trên điện thoại để xác nhận.")
        print("-" * 50)
        print("⏳ Cửa sổ sẽ duy trì mở trong 5 phút để bạn thoải mái thao tác...")
        print("💡 Lưu ý: Khi nào đồng bộ xong, bạn có thể TỰ TAY TẮT cửa sổ Chromium đi, script sẽ tự nhận diện tắt theo.")
        
        # Chờ 5 phút (300 giây) hoặc thoát sớm nếu user tự tắt cửa sổ
        try:
            for _ in range(300):
                time.sleep(1)
                if page.is_closed():
                    break
            if not page.is_closed():
                print("⏳ Hết 5 phút chờ, đang tự động đóng trình duyệt...")
                browser.close()
        except Exception:
            pass
            
        print("👋 Quá trình đồng bộ profile đã đóng. Giờ bạn có thể chạy các tool Zalo Userbot bình thường!")

if __name__ == '__main__':
    run_sync()
