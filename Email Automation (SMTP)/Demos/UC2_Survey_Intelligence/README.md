# UC2: 🧠 Phân Tích Phản Hồi Khách Hàng (Survey Intelligence)

## 🎯 Bối Cảnh Demo
Sau đợt khảo sát dịch vụ, bạn nhận được 20 thư phản hồi trong hòm thư. Bình thường, bạn sẽ phải mở từng thư, đọc và ghi lại ý kiến vào file Excel. 
Nhiệm vụ của bạn là để Robot:
- Tự động đăng nhập vào Inbox.
- Quét nội dung phản hồi của từng khách hàng.
- Phân tích cảm xúc (Sentiment Analysis) cơ bản để gắn thẻ: `Tích cực` (Amazing, Good) hoặc `Cần xử lý` (Bad, Terrible).
- Cập nhật trạng thái này vào file `survey_results.csv`.

## 🚀 Quy Trình Xử Lý Thông Minh (2 Bước)
Để tránh xử lý nhầm dữ liệu, Agent sẽ hoạt động theo quy trình "Quét trước - Duyệt sau":

### Bước 1: 🔍 Quét & Lập Danh Sách (Discovery Phase)
Mục tiêu: Tìm kiếm và trích xuất thông tin cơ bản (Tiêu đề, Người gửi, Đính kèm) để bạn kiểm tra trước khi AI tốn tài nguyên xử lý sâu.

> [!TIP]
> **🤖 Prompt Mẫu cho Bước 1 (2 cách tiếp cận):**
> - **Cách A (Theo thời gian):** *"Quét toàn bộ hòm thư Inbox trong **7 ngày qua**. Tổng hợp danh sách email vào file `discovery_log.csv` (Cột: ID, Tiêu đề, Người gửi, Có file đính kèm không)."*
> - **Cách B (Theo từ khóa):** *"Tìm các email có chứa từ khóa **'[DEMO UC2]'** hoặc **'Feedback'**. Lưu kết quả vào file `discovery_log.csv` để tôi kiểm duyệt."*

### Bước 2: 🧠 Xử Lý Sâu & Phân Tích (Deep Processing Phase)
Mục tiêu: Đọc nội dung chi tiết, phân tích AI và thực hiện hành động (Trả lời hoặc Lưu trữ).

> [!TIP]
> **🤖 Prompt Mẫu cho Bước 2:**
> - *"Dựa vào danh sách trong file `discovery_log.csv`, hãy đánh giá xem email nào có chủ đề liên quan tới feedback của user cho sản phẩm của tôi. Hãy tải nội dung chi tiết của từng email. Phân tích cảm xúc: Nếu là **'Negative'** (Tiêu cực), hãy đánh dấu sao email đó; nếu là **'Positive'** (Tích cực), hãy cập nhật thông tin vào file `survey_results.csv`."*

## 📊 Kết Quả Đạt Được
- **Tiết kiệm tài nguyên:** Chỉ xử lý những email thực sự cần thiết.
- **Kiểm soát tuyệt đối:** Bạn có thể xem file `discovery_log.csv` trước khi cho Robot thực hiện bước xử lý sâu tiếp theo.

## 📊 Dấu Ấn "Siêu Năng Lực"
- **Thấu hiểu ngôn ngữ:** Agent không chỉ đếm từ khóa, nó hiểu được sắc thái của câu chữ.
- **Tự động hóa báo cáo:** Bạn không cần đọc từng thư, chỉ cần xem báo cáo tổng hợp cuối ngày.
