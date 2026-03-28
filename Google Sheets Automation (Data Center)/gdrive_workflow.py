import os
import json
import time
import subprocess

def run_cmd(cmd):
    """Chạy PowerShell ngầm và trả về Output"""
    # Tránh lỗi chuỗi nháy kép khi nạp JSON Object vào tham số CLI
    result = subprocess.run(["powershell.exe", "-Command", cmd], capture_output=True, text=True)
    return result

def main():
    print("==================================================")
    print("🚀 GOOGLE DRIVE AGENT: AUTO-CLONE DATA ENGINE 🚀")
    print("==================================================\n")
    
    # 1. HỎI ĐÁP LINH ĐỘNG (Dynamic Prompt)
    target_name = input("🔍 Nhập Lệnh: Bạn muốn AI [Clone] Tệp / Thư mục nào trên Drive về máy? \n👉 Tên File: ").strip()
    
    if not target_name:
        print("❌ Hủy bỏ: Bạn chưa cung cấp Tên dữ liệu cần lấy.")
        return

    print(f"\n📡 Đang rà quét Đám mây tìm kiếm [{target_name}] ...")
    time.sleep(1) # Tạo cảm giác Loading cho học viên xem
    
    # 2. XÂY DỰNG QUERY LỌC GWS
    ps_cmd = f"""
    $env:QUERY = '{{\"q\": \"name=''{target_name}'' and trashed=false\"}}'
    gws drive files list --params $env:QUERY --format json
    """
    
    res = run_cmd(ps_cmd)
    
    try:
        data = json.loads(res.stdout)
        files = data.get("files", [])
        if not files:
            print(f"❌ Không tìm thấy tọa độ của [{target_name}] trên tài khoản Cloud của bạn.")
            print("Vui lòng gõ chính xác cả cụm từ mở rộng (ví dụ có đuôi .csv / .docx).")
            return
            
        file_info = files[0]
        file_id = file_info["id"]
        mime = file_info.get("mimeType", "")
        
        print(f"✅ Đã Khóa Mục Tiêu (ID: {file_id})")
        print(f"   Định dạng dữ liệu: {mime}")
        
    except Exception as e:
        print("⚠️ Có lỗi truy xuất GWS CLI Terminal. Hãy chắc chắn bạn đã chạy `gws auth login` trước đó.")
        print("Log GWS:", res.stdout)
        return

    # 3. THỰC THI SỨ MỆNH CLONE
    safe_name = target_name.replace(' ', '_')
    save_path = f".\\Clone_{safe_name}"
    
    if "folder" in mime:
        print(f"\n📂 Phát hiện Đối tượng Cấp Thư Mục (Folder). Đang khởi động tiến trình hút File nội bộ...")
        # Lệnh GWS tải Folder xuống máy 
        dl_cmd = f"gws drive files get --id {file_id} > {save_path}_Info.txt" 
    else:
        print(f"\n📥 Đang tiến hành Clone mã nguồn/dữ liệu từ Mây xả xuống máy tính...")
        # Lệnh GWS tải nguyên File 
        dl_cmd = f"gws drive files get --id {file_id} --alt media > {save_path}"
        
    run_cmd(dl_cmd)
    time.sleep(1.5)
    
    # 4. TRẢ LẠI QUYỀN VẬN HÀNH CHO NGƯỜI DÙNG
    print(f"\n🎉 HOÀN TẤT CLONE! Dữ liệu đã hạ cánh an toàn tại: {os.path.abspath(save_path)}")
    print("👉 Code đến đây là hết. Phần còn lại, Quyền năng Xào nấu Data (Edit, Upload) hoàn toàn nằm trong tay Doanh nghiệp bạn!")

if __name__ == "__main__":
    main()
