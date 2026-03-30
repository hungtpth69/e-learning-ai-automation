import os
import glob
import time
import csv
import json

RAW_DIR = "Raw_Documents"
OUTPUT_FILE = "data.js"

def parse_text_documents():
    docs = []
    files = glob.glob(f"{RAW_DIR}/*.txt")
    for idx, filepath in enumerate(files):
        filename = os.path.basename(filepath).replace(".txt", "").replace("_", " ")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        preview = (content[:150] + '...') if len(content) > 150 else content
        safe_id = f"doc_{idx}"
        
        docs.append({
            "id": safe_id,
            "title": filename,
            "preview": preview,
            "content": content
        })
    return docs

def parse_csv_directory():
    contacts = []
    csv_files = glob.glob(f"{RAW_DIR}/*.csv")
    if not csv_files:
        return []
        
    filepath = csv_files[0]
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_row = {k.strip(): v.strip() for k, v in row.items() if k}
            contacts.append(cleaned_row)
            
    return contacts

def main():
    print("======================================================")
    print("🚀 TỐI ƯU HÓA DATA CHO AGENT (OPTIMIZED RAW INPUT) 🚀")
    print("======================================================\n")
    
    if not os.path.exists(RAW_DIR):
        print(f"❌ Thư mục '{RAW_DIR}' chưa tồn tại. Hệ thống đã tự động tạo mới.")
        os.makedirs(RAW_DIR, exist_ok=True)
        print(f"⚠️ Vui lòng đưa các file bài viết (.txt) và danh bạ (.csv) vào '{RAW_DIR}' rồi chạy lại nhé.")
        return
        
    print(f"🔍 [System] Bước 1: Thu thập Dữ liệu Text phân mảnh tại '{RAW_DIR}'...")
    time.sleep(1)
    docs = parse_text_documents()
    print(f"   -> Đã trích xuất {len(docs)} tài liệu.")
    
    print(f"🔍 [System] Bước 2: Thu thập Dữ liệu Danh bạ CSV trong '{RAW_DIR}'...")
    time.sleep(1)
    contacts = parse_csv_directory()
    print(f"   -> Đã trích xuất {len(contacts)} người dùng.")
    
    print("🧠 [System] Bước 3: Đóng gói toàn bộ Data thành Cấu Trúc Khối `data.js`...")
    time.sleep(1)
    
    data_payload = {
        "documents": docs,
        "contacts": contacts
    }
    
    js_content = "const portalData = " + json.dumps(data_payload, ensure_ascii=False, indent=4) + ";"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"\n✅ HOÀN TẤT! Đã cô đặc dòng chảy dữ liệu vào file `{OUTPUT_FILE}`.")
    print("======================================================")
    print("🔥 BƯỚC CUỐI CÙNG: RA LỆNH CHO TRÍ TUỆ NHÂN TẠO (AI IDE)")
    print("👉 Code UI không bị giới hạn bởi Template nữa! Bạn hãy Copy nguyên văn câu lệnh Prompt dưới đây và gửi cho Khung Chat Trợ lý ảo Antigravity AI để nó tự Code Web cho bạn:\n")
    print("-" * 75)
    print("Hãy đọc dữ liệu từ file `data.js` hiện tại và đóng vai một Kỹ sư Thiết kế Kiến trúc Web siêu cấp.")
    print("Nhiệm vụ: Lập trình ngay cho tôi 1 file `index.html` tuyệt đẹp chứa toàn bộ Data này.")
    print("Yêu cầu:")
    print("1. Dùng Tailwind CSS CDN và Vanilla JS viết nội tuyến (tất cả chỉ trong 1 file).")
    print("2. Giao diện Light Mode, phong cách Glassmorphism ma thuật (nền tối, bóng mờ).")
    print("3. Có Navigation chuyển đổi qua lại giữa 'Kho Tài Liệu' và 'Danh Bạ Nhân Sự'.")
    print("4. Render Data JSON ra thành Lưới Thẻ Bài (Grid Cards) với đầy đủ nội dung.")
    print("5. Thêm tính năng 1 Thanh Tìm Kiếm Động (Search Bar) lọc dữ liệu bằng JS.")
    print("Tôi chỉ cần Code, không cần giải thích! Hãy xuất luôn File đi!")
    print("-" * 75)

if __name__ == "__main__":
    main()
