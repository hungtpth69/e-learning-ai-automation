import requests
import csv
import time
import os

# ==============================================================
# 🎯 CẤU HÌNH ZALO OA API
# ==============================================================
ZALO_OA_ACCESS_TOKEN = ""
if os.path.exists("zalo_token.txt"):
    with open("zalo_token.txt", "r", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.strip().split('=', 1)
                if k.strip() == "ZALO_OA_ACCESS_TOKEN":
                    ZALO_OA_ACCESS_TOKEN = v.strip('"\' ')

FILE_INPUT_CSV = "zalo_contact_list.csv"
FILE_LOG_CSV = "zalo_oa_log.csv"

def skill_read_data():
    print("🤖 [Agent] Kích hoạt skill_read_data()...")
    danh_sach = []
    if os.path.exists(FILE_INPUT_CSV):
        with open(FILE_INPUT_CSV, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                danh_sach.append(row)
    return danh_sach

def skill_generate_message(ho_ten, noi_dung_tuy_chinh):
    print(f"🧠 [Agent] Soạn thông điệp cho: {ho_ten}...")
    time.sleep(0.5) 
    return f"👋 Kính gửi {ho_ten},\n\n{noi_dung_tuy_chinh}\n\n(Phát đi từ Zalo Official Account Doanh Nghiệp)"

def skill_notify_zalo_oa(user_id, noi_dung):
    """Kỹ năng gọi API ẩn danh của Zalo Doanh Nghiệp"""
    url = "https://openapi.zalo.me/v3.0/oa/message/cs"
    headers = {
        "access_token": ZALO_OA_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "recipient": {"user_id": str(user_id).strip()},
        "message": {"text": noi_dung}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": -1, "message": str(e)}

def skill_log_result(ho_ten, user_id, trang_thai):
    mode = 'a' if os.path.exists(FILE_LOG_CSV) else 'w'
    with open(FILE_LOG_CSV, mode=mode, encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        if mode == 'w':
            writer.writerow(["Thoi_Gian", "Ho_Ten", "Zalo_User_ID", "Ket_Qua_Trang_Thai"])
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), ho_ten, user_id, trang_thai])

def main():
    print("======================================================")
    print("🛸 HỆ THỐNG AGENT WORKFLOW: ZALO OA TỰ ĐỘNG (API) 🛸")
    print("======================================================\n")
    
    danh_sach = skill_read_data()
    if not danh_sach:
        print("❌ Data rỗng!")
        return
        
    print("\n🚀 BẮT ĐẦU CHUỖI XỬ LÝ WORKFLOW ĐA BƯỚC...\n")

    for contact in danh_sach:
        ten = contact.get('Ho_Ten', '')
        user_id = contact.get('Zalo_User_ID', '')
        noi_dung_raw = contact.get('Noi_Dung_Tuy_Chinh', '')

        if not user_id: # OA bắt buộc dùng ID ẩn danh
            continue
            
        print("-" * 50)
        tin_nhan = skill_generate_message(ten, noi_dung_raw)
        print(f"📨 [Agent] Đang đẩy Payload API Zalo OA tới ID [{user_id}]...")
        
        ket_qua = skill_notify_zalo_oa(user_id, tin_nhan)
        error_code = ket_qua.get("error", -1)
        
        if error_code == 0:
            print(f"  [➔] THÀNH CÔNG ➞ Đã gửi cho: {ten}")
            trang_thai_log = "Thành Công"
        else:
            msg = ket_qua.get("message", "Lỗi Cú pháp / Thiếu Token")
            print(f"  [✖] THẤT BẠI ➞ Lỗi kết nối tài khoản {ten}: {msg[:50]}")
            trang_thai_log = f"Lỗi: {msg}"

        skill_log_result(ten, user_id, trang_thai_log)
        time.sleep(0.5) # Chống Spam

    print("-" * 50)
    print("🎉 HOÀN TẤT CHIẾN DỊCH ZALO OA!")

if __name__ == "__main__":
    main()
