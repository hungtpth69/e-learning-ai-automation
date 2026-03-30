---
description: Tự động hóa nén dữ liệu thô và Build Web Portal (index.html) cho Vercel
---

Quy trình này hướng dẫn Agent (trợ lý ảo) tự động hóa việc thu thập, nén các dữ liệu thô (văn bản tài liệu, danh bạ) trong dự án thành cấu trúc dữ liệu web (như JSON hoặc .js), sau đó tự động viết và xuất bản một file `index.html` dùng làm trang chủ để public tài liệu lên Vercel.

// turbo-all

1. Tìm và chạy Script Nén Dữ Liệu
Agent hãy tìm trong dự án (ưu tiên thư mục `\Internal Portal (Vercel Deploy)`) một file python chịu trách nhiệm nén dữ liệu (ví dụ: `optimized_raw_input.py`). Nếu không thấy, hãy chủ động search file liên quan.
Sau khi tìm thấy, chạy script đó để biến file thô thành khối dữ liệu (ví dụ `data.js`).
```bash
cd "e:\Antigravity\e-learning\Internal Portal (Vercel Deploy)"
python optimized_raw_input.py
```

2. Tạo Website Giao Diện (index.html)
Sau khi có được file dữ liệu (`data.js`), Agent hãy dùng quyền năng tự động lập trình để cấu trúc một file `index.html` siêu đẹp, hiện đại (ví dụ dùng Tailwind CSS, thiết kế Dark/Glassmorphism, tích hợp tính năng Tìm kiếm và Lọc nội dung bằng JS nội tuyến). 
Hãy lưu `index.html` trực tiếp vào cùng thư mục. Web phải hiển thị được toàn bộ nội dung từ `data.js` mà không bị gián đoạn.

3. Kiểm Tra & Báo Cáo
Kiểm tra xem các file cốt lõi (`data.js` và `index.html`) đã tồn tại ở trạng thái sẵn sàng chưa.
Báo cáo cho người dùng biết kết quả (thành công/thất bại) kèm theo hướng dẫn ngắn để họ preview file web hoặc chuẩn bị đưa lên Vercel.