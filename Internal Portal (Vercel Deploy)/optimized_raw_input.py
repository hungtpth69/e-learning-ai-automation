import os
import glob
import time
import csv
import json

RAW_DIR = "Raw_Documents"
OUTPUT_FILE = "data.js"

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic AI Vision Board | Antigravity AI Engine</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: 'Outfit', sans-serif; background: #0f172a; color: #f8fafc; overflow-x: hidden; }
        .glass-panel {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .orb {
            position: fixed; border-radius: 50%; filter: blur(100px); z-index: -1; opacity: 0.6;
            animation: float 20s infinite alternate cubic-bezier(0.4, 0, 0.2, 1);
        }
        .orb-1 { width: 500px; height: 500px; background: #6366f1; top: -100px; left: -100px; }
        .orb-2 { width: 400px; height: 400px; background: #ec4899; bottom: -50px; right: -50px; animation-duration: 25s; }
        
        @keyframes float { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(150px, 100px) scale(1.2); } }
        
        .card-hover { transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }
        .card-hover:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 20px 40px rgba(99, 102, 241, 0.2); border-color: rgba(99, 102, 241, 0.5); }
        
        .tab-btn { position: relative; transition: all 0.3s ease; }
        .tab-btn::after {
            content: ''; position: absolute; bottom: -4px; left: 50%; transform: translateX(-50%); width: 0; height: 3px; background: #6366f1; border-radius: 3px; transition: width 0.3s ease;
        }
        .tab-btn.active { color: white; text-shadow: 0 0 10px rgba(255,255,255,0.3); }
        .tab-btn.active::after { width: 100%; }
        
        .content-section { display: none; opacity: 0; animation: fadeIn 0.5s ease forwards; }
        .content-section.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

        /* Loader */
        #loader { display: flex; position: fixed; inset: 0; background: #0f172a; z-index: 50; flex-direction: column; align-items: center; justify-content: center; transition: 0.8s; }
        .ai-core { width: 80px; height: 80px; border-radius: 50%; background: conic-gradient(from 0deg, transparent, #ec4899, #6366f1, transparent); animation: spin 1s infinite linear; border: 4px solid rgba(255,255,255,0.1); box-shadow: 0 0 50px rgba(99,102,241,0.5); }
        @keyframes spin { 100% { transform: rotate(360px); } }
    </style>
</head>
<body class="min-h-screen">
    <!-- Dynamically Injected Data -->
    <script src="data.js"></script>

    <div id="loader">
        <div class="ai-core"></div>
        <p class="mt-8 text-xl font-semibold tracking-widest text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-indigo-400">AGENT IS PROCESSING DATA.JS</p>
    </div>

    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>

    <div class="max-w-7xl mx-auto px-6 py-12 relative z-10 hidden" id="app">
        
        <header class="flex justify-between items-center mb-16 glass-panel p-6 rounded-3xl">
            <div class="flex items-center gap-4">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-indigo-500 to-pink-500 flex items-center justify-center text-2xl shadow-lg">
                    <i class="fa-solid fa-brain"></i>
                </div>
                <div>
                    <h1 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">Antigravity Hub</h1>
                    <p class="text-sm text-indigo-300 font-medium">Dynamic AI-Generated Portal</p>
                </div>
            </div>
            <nav class="flex gap-8">
                <button class="tab-btn active text-gray-400 font-semibold text-lg" onclick="switchTab('docs', this)">Tài Liệu Cốt Lõi</button>
                <button class="tab-btn text-gray-400 font-semibold text-lg" onclick="switchTab('contacts', this)">Mạng Lưới Chuyên Gia</button>
            </nav>
        </header>

        <!-- VIEW 1: DOCUMENTS -->
        <main id="docs" class="content-section active">
            <div class="flex justify-between items-end mb-10">
                <div>
                    <h2 class="text-4xl font-bold mb-2">Kho Tàng Tri Thức</h2>
                    <p class="text-gray-400 text-lg">Được phân rã từ luồng xử lý Natural Language Processing</p>
                </div>
                <div class="relative w-80">
                    <i class="fa-solid fa-magnifying-glass absolute left-4 top-1/2 -translate-y-1/2 text-gray-400"></i>
                    <input type="text" id="searchInput" onkeyup="searchDocs()" placeholder="Tìm kiếm văn bản không giới hạn..." 
                        class="w-full bg-slate-800/50 border border-slate-600 rounded-xl py-3 pl-12 pr-4 text-white focus:outline-none focus:border-indigo-400 focus:ring-1 focus:ring-indigo-400 transition-all placeholder:text-gray-500">
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="docsGrid">
                <!-- Dynamically generated -->
            </div>
        </main>

        <!-- VIEW 2: FULL READER -->
        <main id="reader" class="content-section">
            <button onclick="switchTab('docs', document.querySelectorAll('.tab-btn')[0])" class="mb-8 px-5 py-2.5 rounded-xl glass-panel text-white font-medium hover:bg-slate-700 transition flex items-center gap-3">
                <i class="fa-solid fa-arrow-left"></i> Rời khỏi Buồng Đọc
            </button>
            <div class="glass-panel p-12 rounded-3xl relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"></div>
                <h1 id="readerTitle" class="text-4xl font-bold mb-8 text-white capitalize"></h1>
                <div class="w-full h-[1px] bg-slate-700/50 mb-8"></div>
                <div id="readerContent" class="text-lg text-slate-300 leading-relaxed font-light whitespace-pre-wrap text-justify"></div>
            </div>
        </main>

        <!-- VIEW 3: DIRECTORY -->
        <main id="contacts" class="content-section">
            <h2 class="text-4xl font-bold mb-2">Nhân Tử Nền Tảng</h2>
            <p class="text-gray-400 text-lg mb-10">Danh sách nhân sự trích xuất từ Data Lake CSV</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="contactsGrid">
                <!-- Dynamically Build -->
            </div>
        </main>

        <footer class="mt-24 text-center text-slate-500 text-sm">
            <p>Code HTML/CSS được sinh động lập tức bằng tư duy LLM, miễn nhiễm với mọi giới hạn Template.</p>
        </footer>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                document.getElementById('loader').style.opacity = '0';
                setTimeout(() => {
                    document.getElementById('loader').style.display = 'none';
                    document.getElementById('app').classList.remove('hidden');
                }, 800);
            }, 1200);

            if (typeof portalData === 'undefined') {
                document.getElementById('docsGrid').innerHTML = '<p class="text-red-400 font-bold col-span-full border border-red-500/30 bg-red-500/10 p-4 rounded-xl">⚠️ FATAL ERROR: Chưa tìm thấy mạch dữ liệu data.js! Vui lòng chạy Python Compiler trước.</p>';
            } else {
                buildIntelligence(portalData);
            }
        });

        function switchTab(viewId, btnEl) {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            if(btnEl) btnEl.classList.add('active');

            document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
            document.getElementById(viewId).classList.add('active');
        }

        function buildIntelligence(data) {
            // Build Documents
            const docsGrid = document.getElementById('docsGrid');
            if(data.documents.length === 0) docsGrid.innerHTML = '<p class="text-slate-400">Không có dữ kiện văn bản.</p>';
            
            data.documents.forEach((doc, i) => {
                const colors = ['from-indigo-500 to-cyan-500', 'from-purple-500 to-pink-500', 'from-orange-400 to-rose-400'];
                const card = document.createElement('div');
                card.className = 'glass-panel rounded-2xl p-8 card-hover flex flex-col doc-card';
                card.innerHTML = `
                    <div class="w-14 h-14 rounded-full bg-gradient-to-tr ${colors[i%3]} flex items-center justify-center text-white text-xl mb-6 shadow-lg shadow-indigo-500/20">
                        <i class="fa-solid fa-file-code"></i>
                    </div>
                    <h3 class="text-2xl font-bold mb-4 text-white capitalize">${doc.title}</h3>
                    <p class="text-slate-400 text-sm mb-8 flex-grow leading-relaxed">${doc.preview}</p>
                    <button onclick="readDoc('${doc.id}')" class="w-full py-3 rounded-xl border border-indigo-500/50 text-indigo-300 font-semibold hover:bg-indigo-500 hover:text-white transition-all">
                        Giải nén toàn văn
                    </button>
                `;
                docsGrid.appendChild(card);
            });

            // Build Contacts Extracted from Schema-less Logic
            const contactsGrid = document.getElementById('contactsGrid');
            if(data.contacts.length === 0) {
                contactsGrid.innerHTML = '<p class="text-slate-400 col-span-full">Tệp liên lạc trống rỗng.</p>';
            }

            data.contacts.forEach(contact => {
                const keys = Object.keys(contact);
                if(keys.length === 0) return;

                const name = contact[keys[0]] || 'Unknown Entity';
                const role = keys.length > 1 ? contact[keys[1]] : 'Member';
                
                let hash = 0; for(let i=0; i<name.length; i++) hash = name.charCodeAt(i) + ((hash<<5)-hash);
                const color = Math.abs(hash).toString(16).substring(0,6).padStart(6,'0');

                let details = '';
                keys.slice(2).forEach(k => {
                    if(contact[k]) {
                        details += `<div class="flex flex-col mb-3"><span class="text-[10px] uppercase tracking-wider text-slate-500 font-bold mb-1">${k.replace(/_/g,' ')}</span><span class="text-sm text-slate-300 break-words">${contact[k]}</span></div>`;
                    }
                });

                const card = document.createElement('div');
                card.className = 'glass-panel rounded-2xl p-6 flex flex-col card-hover border-t-2 border-t-indigo-500';
                card.innerHTML = `
                    <div class="flex items-center gap-4 mb-6">
                        <img src="https://ui-avatars.com/api/?name=${encodeURIComponent(name)}&background=${color}&color=fff" class="w-14 h-14 rounded-full border-2 border-white/10">
                        <div>
                            <h3 class="font-bold text-lg text-white">${name}</h3>
                            <span class="text-xs px-2 py-1 bg-indigo-500/20 text-indigo-300 rounded-md font-semibold">${role}</span>
                        </div>
                    </div>
                    <div class="w-full h-[1px] bg-slate-700 mb-4"></div>
                    <div class="flex-grow space-y-2">
                        ${details}
                    </div>
                `;
                contactsGrid.appendChild(card);
            });
        }

        function readDoc(id) {
            const doc = portalData.documents.find(d => d.id === id);
            if(doc) {
                document.getElementById('readerTitle').innerText = doc.title;
                document.getElementById('readerContent').innerText = doc.content;
                switchTab('reader', null);
            }
        }

        function searchDocs() {
            const val = document.getElementById('searchInput').value.toLowerCase();
            document.querySelectorAll('.doc-card').forEach(card => {
                const title = card.querySelector('h3').innerText.toLowerCase();
                card.style.display = title.includes(val) ? 'flex' : 'none';
            });
        }
    </script>
</body>
</html>"""

def check_and_restore_html():
    if not os.path.exists("index.html"):
        print("\n⚠️ [Agent] Phát hiện thiếu file giao diện `index.html`! Đang tự động triển khai bản gốc...")
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE)
        print("✅ Đã khôi phục thành công file `index.html` bằng Template Kính Toàn Năng (Glassmorphism)!")
    else:
        print("\n💡 [Agent] File `index.html` đã tồn tại an toàn. Đã ngắt cơ chế ghi đè để bảo vệ tuỳ biến của bạn.")

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
    print("🚀 OFFLINE DATA COMPILER: TỐI ƯU HÓA DỮ LIỆU ĐẦU VÀO 🚀")
    print("======================================================\n")
    
    # 1. Tự động đẻ Web UI nếu lỡ tay làm mất
    check_and_restore_html()
    
    if not os.path.exists(RAW_DIR):
        print(f"❌ Thư mục '{RAW_DIR}' chưa tồn tại. Hệ thống đã tự động tạo mới.")
        os.makedirs(RAW_DIR, exist_ok=True)
        print(f"⚠️ Vui lòng đưa các file bài viết (.txt) và danh bạ (.csv) vào '{RAW_DIR}' rồi chạy lại nhé.")
        return
        
    print(f"🔍 [Agent] Bước 1: Thu thập Dữ liệu Text phân mảnh tại '{RAW_DIR}'...")
    time.sleep(1)
    docs = parse_text_documents()
    print(f"   -> Đã trích xuất {len(docs)} tài liệu.")
    
    print(f"🔍 [Agent] Bước 2: Thu thập Dữ liệu Danh bạ CSV trong '{RAW_DIR}'...")
    time.sleep(1)
    contacts = parse_csv_directory()
    print(f"   -> Đã trích xuất {len(contacts)} người dùng.")
    
    print("🧠 [Agent] Bước 3: Đóng gói toàn bộ Data thành Cấu Trúc Khối Vandal `data.js`...")
    time.sleep(1)
    
    data_payload = {
        "documents": docs,
        "contacts": contacts
    }
    
    js_content = "const portalData = " + json.dumps(data_payload, ensure_ascii=False, indent=4) + ";"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"\n✅ HOÀN TẤT! Đã siêu nén toàn bộ dữ liệu thô vào file `{OUTPUT_FILE}` thành công!")
    print("👉 Hãy nhấp đúp file `index.html` nằm cạnh file này bằng Google Chrome để chiêm ngưỡng Dynamic Web UI vô hạn!")

if __name__ == "__main__":
    main()
