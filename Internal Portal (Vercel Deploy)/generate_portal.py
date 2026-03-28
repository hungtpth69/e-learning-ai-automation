import os
import glob
import time
import csv

RAW_DIR = "Raw_Documents"
OUTPUT_FILE = "index.html"

def generate_detail_page(filename, content):
    """Sinh ra Trang Đọc Chi Tiết (Subpage) cho từng bài viết"""
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename} | Antigravity Hub</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="app-background"></div>
    <div class="glass-container" style="display: block; padding: 40px; overflow-y: auto;">
        <a href="index.html" style="text-decoration: none; color: var(--primary); font-weight: bold; padding: 10px 20px; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);"><i class="fa-solid fa-arrow-left"></i> Quay lại Bảng Tin</a>
        
        <h1 style="color: var(--text-main); margin: 30px 0 20px 0; font-size: 28px; text-transform: uppercase;">{filename}</h1>
        
        <div style="background: rgba(255,255,255,0.7); padding: 40px; border-radius: 16px; font-size: 16px; line-height: 1.8; color: #334155; white-space: pre-wrap; box-shadow: 0 4px 6px rgba(0,0,0,0.02); border: 1px solid var(--border);">
{content}
        </div>
        
        <div style="margin-top: 40px; text-align: center; color: var(--text-muted); font-size: 13px;">
            Văn bản được số hóa nguyên bản tự động bởi Antigravity AI SSG Engine.
        </div>
    </div>
</body>
</html>"""
    
    # Định dạng tên file an toàn: Bỏ dấu cách, thêm đuôi html
    safe_name = filename.replace(" ", "_").lower()
    out_name = f"doc_{safe_name}.html"
    
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(html)
        
    return out_name

def read_text_documents():
    """Hàm xử lý Văn Bản Thô (TXT) và tạo Link liên kết URL"""
    html_cards = ""
    colors = ["blue", "green", "purple", "orange", "red"]
    icons = ["fa-file-contract", "fa-calendar-check", "fa-shield-halved", "fa-envelope-open-text", "fa-file-invoice"]
    
    files = glob.glob(f"{RAW_DIR}/*.txt")
    if not files:
        return "<p>Chưa có tài liệu text nào.</p>", 0
        
    for idx, filepath in enumerate(files):
        filename = os.path.basename(filepath).replace(".txt", "").replace("_", " ")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        # Gọi hàm đẻ file Subpage riêng lẻ và lấy Link
        subpage_url = generate_detail_page(filename, content)
        
        preview = (content[:150] + '...') if len(content) > 150 else content
        color = colors[idx % len(colors)]
        icon = icons[idx % len(icons)]
        
        # Thẻ Card nay đã gắn Link <a> thực sự hướng vào Subpage
        card = f"""
        <div class="stat-card" style="transition: 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <div class="card-icon {color}"><i class="fa-solid {icon}"></i></div>
            <div style="flex-grow: 1;">
                <h3 style="text-transform: capitalize;">{filename}</h3>
                <p style="text-align: justify; font-size: 13px; line-height: 1.6; margin-bottom: 12px;">{preview}</p>
                <a href="{subpage_url}" style="display: inline-block; padding: 6px 16px;text-decoration: none; background: #e2e8f0; border-radius: 6px; font-size: 13px; font-weight: 700; color: var(--text-main); transition: 0.2s;" onmouseover="this.style.background='var(--primary)'; this.style.color='white'" onmouseout="this.style.background='#e2e8f0'; this.style.color='var(--text-main)'">Đọc toàn văn <i class="fa-solid fa-arrow-right"></i></a>
            </div>
        </div>
        """
        html_cards += card
        
    return html_cards, len(files)

def read_csv_directory():
    """Hàm xử lý Danh Bạ Nhân Sự (CSV)"""
    html_cards = ""
    filepath = f"{RAW_DIR}/Danh_Ba_Nhan_Vien.csv"
    
    if not os.path.exists(filepath):
        return "<p>Chưa nạp file Danh_Ba_Nhan_Vien.csv.</p>"
        
    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ten = row.get("Ho_Ten", "Không Tên")
            chuc_vu = row.get("Chuc_Vu", "")
            phong_ban = row.get("Phong_Ban", "")
            email = row.get("Email", "")
            sdt = row.get("So_Dien_Thoai", "")
            
            bg = str(hash(ten) % 999999)[0:6]
            
            card = f"""
            <div class="stat-card" style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 10px;">
                <img src="https://ui-avatars.com/api/?name={ten.replace(' ', '+')}&background={bg}&color=fff&size=80" style="border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
                <div>
                    <h3 style="font-size: 17px; margin-bottom: 5px; color: var(--text-main); font-weight: 700;">{ten}</h3>
                    <span style="background: var(--bg-color); color: var(--primary); font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 20px; border: 1px solid #c7d2fe;">{chuc_vu}</span>
                    <p style="margin-top: 10px; font-size: 14px; color: var(--text-muted);"><i class="fa-solid fa-briefcase"></i> {phong_ban}</p>
                    <hr style="margin: 15px 0; border: none; border-top: 1px dashed var(--border);">
                    <p style="font-size: 13px; color: var(--text-main);"><i class="fa-solid fa-envelope"></i> {email}</p>
                    <p style="font-size: 13px; color: var(--text-main); margin-top: 5px;"><i class="fa-solid fa-phone"></i> {sdt}</p>
                </div>
            </div>
            """
            html_cards += card
    return html_cards

def generate_base_html(doc_cards, dir_cards):
    """Gen Main Layout: Lược bỏ toàn bộ UI thừa (Search giả, Nút chuông giả)"""
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cổng Thông Tin Nội Bộ | Antigravity AI</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="app-background"></div>
    <div class="glass-container">
        
        <!-- SIDEBAR GIAO DIỆN -->
        <nav class="sidebar">
            <div class="logo">
                <i class="fa-solid fa-shapes"></i>
                <span>Antigravity Hub</span>
            </div>
            
            <p class="menu-label">MENU CHÍNH</p>
            <ul class="nav-links">
                <li class="active" onclick="switchTab('dashboard', this)"><i class="fa-solid fa-folder-open"></i> Kho Tài Liệu Số</li>
                <li onclick="switchTab('directory', this)"><i class="fa-solid fa-address-book"></i> Danh bạ Nhân sự</li>
            </ul>

            <div class="user-profile">
                <img src="https://ui-avatars.com/api/?name=Admin+User&background=6366f1&color=fff" alt="User">
                <div class="user-info">
                    <h4>Toàn thể Cán bộ NV</h4>
                    <p>Internal Viewer</p>
                </div>
            </div>
        </nav>

        <!-- MAIN CONTENT CHÍNH -->
        <main class="main-content" style="padding-top: 40px;">
            <section id="dashboard" class="tab-content active-tab">
                <div class="welcome-banner">
                    <div class="banner-text">
                        <h1>Cổng Đồng Bộ Kiến Thức 2026</h1>
                        <p>Hệ thống Web được khởi tạo động (Generator) tự động tổng hợp Tài liệu chữ (Text), Danh bạ (CSV) đúc thành trang thông tin trực quan tương tác toàn phần.</p>
                    </div>
                </div>

                <h2 class="section-title" style="margin-top: 30px;">Tài Liệu Văn Bản Nội Bộ</h2>
                <div class="cards-grid">
                    {doc_cards}
                </div>
            </section>

             <section id="directory" class="tab-content">
                <h2 class="section-title">Danh Bạ Liên Lạc Chuyên Ước</h2>
                <div class="directory-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
                    {dir_cards}
                </div>
            </section>
        </main>
    </div>
    
    <script src="script.js"></script>
</body>
</html>"""
    return html

def main():
    print("======================================================")
    print("🚀 SSG: TIẾN HÀNH ĐÚC PHÂN TRANG (ROUTING HTML SUBPAGES) 🚀")
    print("======================================================\n")
        
    print(f"🔍 [Agent] Bước 1: Quét hệ sinh thái dữ liệu Txt và đúc từng Subpage chứa nội dung Đọc...")
    time.sleep(1)
    doc_cards, count = read_text_documents()
    
    print(f"🔍 [Agent] Bước 2: Quét Danh Bạ Nhân Sự CSV trong `{RAW_DIR}`...")
    time.sleep(1)
    dir_cards = read_csv_directory()
    
    print("🧠 [Agent] Bước 3: Rót 100% Data và nặn ra Menu Index liên kết...")
    time.sleep(1)
    final_html = generate_base_html(doc_cards, dir_cards)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"\n✅ HOÀN TẤT! Đã sinh mã nguồn (Gen-code) thành trang chủ `{OUTPUT_FILE}` và {count} Subpage đọc tài liệu!")
    print("👉 Code đã dọn dẹp sạch UI rác. Các nút bấm thực sự điều hướng qua lại sống động 100%.")
    print("👉 Hãy gõ `/build-portal` và mở thử file `index.html` của bạn để Trải Nghiệm Điều Diệu Kỳ.")

if __name__ == "__main__":
    main()
