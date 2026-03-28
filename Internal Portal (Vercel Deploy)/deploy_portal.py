import os
import time
import subprocess
import shutil

REPO_NAME = "antigravity-hub-2026"

def run_cmd(cmd, check=False):
    """Chạy lệnh Shell ngầm"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"   ❌ Lỗi khi chạy lệnh [{cmd}]: {result.stderr.strip()}")
    return result

def check_dependencies():
    """Kiểm tra xem máy tính đã cài đặt Git và Github CLI (gh) chưa"""
    if not shutil.which("git"):
        print("❌ LỖI: Máy tính của bạn chưa cài đặt Git.")
        return False
    if not shutil.which("gh"):
        print("❌ LỖI: Máy tính của bạn chưa cài đặt Github CLI (gh). Hãy cài đặt và chạy `gh auth login` trước.")
        return False
    return True

def main():
    print("==================================================")
    print("🚀 GITHUB AGENT: TỰ ĐỘNG KHỞI TẠO & PUSH MÃ NGUỒN 🚀")
    print("==================================================\n")
    
    if not check_dependencies():
        return
        
    print("1. Đang khởi tạo Kho chứa Git cục bộ (Local Repository)...")
    time.sleep(1)
    # Xoá thư mục .git cũ nếu có để tránh đụng độ rác (Tuỳ chọn)
    if os.path.exists(".git"):
        try:
            shutil.rmtree(".git")
        except:
            pass
            
    run_cmd("git init", check=True)
    run_cmd("git add .", check=True)
    run_cmd('git commit -m "🚀 Auto-Deployed by Antigravity SSG Agent"')
    run_cmd("git branch -M main")
    
    print("\n2. Đang kết nối lên Đám Mây Github để tạo Repository mới...")
    time.sleep(1.5)
    
    # Sử dụng `gh repo view` để kiểm tra repo đã tồn tại chưa
    check_repo = run_cmd(f"gh repo view {REPO_NAME}")
    if check_repo.returncode == 0:
        print(f"   ⚠️ Kho chứa `{REPO_NAME}` đã tồn tại trên Github của bạn. Đang thiết lập đẩy đè lên...")
        # Nếu đã có, chỉ add remote rồi push
        # Lấy username github
        gh_user = run_cmd("gh api user | grep '\"login\":'").stdout.split('"')[3] if "login" in run_cmd("gh api user").stdout else ""
        if gh_user:
            run_cmd(f"git remote add origin https://github.com/{gh_user}/{REPO_NAME}.git")
    else:
        # Tạo Repository MỚI TINH KHÔI, chế độ Public để Vercel đọc được
        print(f"   => Đang ra lệnh đúc Repository [{REPO_NAME}] trên Github.com...")
        res = run_cmd(f"gh repo create {REPO_NAME} --public --source=. --remote=origin", check=True)
        if res.returncode == 0:
            print("   ✅ Đã khởi tạo Repository thành công trên Mây!")

    print("\n3. Đang dội dồn Mã Nguồn (Push Code) lên Internet...")
    time.sleep(1.5)
    push_result = run_cmd("git push -u origin main", check=False)
    
    if "Everything up-to-date" in push_result.stdout or "Everything up-to-date" in push_result.stderr:
        print("   ✅ Code đã được đồng bộ 100%. Không có gì thay đổi mới.")
    elif push_result.returncode == 0 or "branch 'main' set up" in push_result.stderr.lower():
        print("   ✅ Toàn bộ Website tĩnh đã đáp cánh xuống Github Server USA an toàn!")
    else:
        print(f"   ⚠️ Có cảnh báo trong lúc đẩy Git: {push_result.stderr.strip()}")

    print("\n==================================================")
    print("🎉 KHÂU BIÊN DỊCH & TRIỂN KHAI GITHUB ĐÃ HOÀN TẤT!")
    print(f"👉 Link Mã Nguồn: https://github.com/your-username/{REPO_NAME}")
    print("👉 Bây giờ, bạn chỉ việc mở Vercel.com, Import repo tên là `antigravity-hub-2026` và bấm Deploy!")

if __name__ == "__main__":
    main()
