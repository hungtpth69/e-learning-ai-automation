# UC3: 📁 Trợ Lý Tài Chính (Automated Invoice Extraction)

## 🎯 Bối Cảnh Demo
Mỗi tháng, công ty bạn nhận được hàng chục hóa đơn từ các nhà cung cấp qua email. Nhân viên kế toán bình thường phải:
- Tìm email có đính kèm hóa đơn.
- Tải về.
- Đổi tên file theo đúng chuẩn kế toán: `Hóa_đơn_Tháng_03_Tên_Công_Ty.pdf`.
Nhiệm vụ của bạn là để Robot:
- Tự động lọc các email có tiêu đề liên quan đến "Invoice" (Hóa đơn).
- Tải file đính kèm.
- **Tự động trích xuất thông tin** (Công ty, Tổng tiền, Ngày tháng) từ nội dung thư để đặt lại tên file.
- Lưu trữ vào đúng thư mục kế toán.

## 🚀 Quy Trình Trợ Lý Tài Chính (2 Bước)
Để Đội Kế Toán kiểm soát hóa đơn tốt hơn, Agent thực hiện theo 2 giai đoạn:

### Bước 1: 🔍 Tìm Kiếm & Liệt Kê Hóa Đơn (Indexing)
Mục tiêu: Quét sạch hòm thư để đảm bảo không bỏ sót hóa đơn nào của nhà cung cấp.

> [!TIP]
> **🤖 Prompt Mẫu cho Bước 1:**
> - *"Hãy quét toàn bộ hòm thư trong **tháng này** (từ ngày 01 đến nay). Tìm tất cả Email có file đính kèm và chủ đề chứa từ khóa **'Hóa đơn'** hoặc **'Invoice'**."*
> - *"Lập danh sách các hóa đơn này vào file `invoice_index.csv` (Gồm: Ngày nhận, Tiêu đề, Người gửi, Tên file đính kèm)."*

### Bước 2: 📥 Tải & Chuẩn Hóa Tên File (Action)
Mục tiêu: Đưa hóa đơn về máy tính với tên file dễ tra cứu nhất.

> [!TIP]
> **🤖 Prompt Mẫu cho Bước 2:**
> - *"Sử dụng danh sách từ file `invoice_index.csv`, hãy tiến hành tải toàn bộ file đính kèm về thư mục `Invoices_Folder`."*
> - *"Đối với mỗi file, hãy tự động trích xuất Tên Công Ty và Ngày Tháng từ nội dung email để đổi tên file theo định dạng: `Hoa_don_[Ten_Cong_Ty]_[Ngay_Thang].pdf`."*

## 📊 Thành Quả
- **Quản lý tập trung:** Bạn có một file `invoice_index.csv` để làm bìa danh mục hóa đơn cho cả tháng.
- **Tự động hóa tuyệt đối:** Không còn cảnh mở từng thư để tải và đổi tên thủ công.

## 📊 Dấu Ấn "Siêu Năng Lực"
- **Không nhầm lẫn:** Tên file được chuẩn hóa 100%, dễ dàng tra cứu về sau.
- **Tiết kiệm thời gian:** Thay vì tốn 2 phút cho mỗi hóa đơn, Robot làm hàng chục cái chỉ trong 2 giây.
- **Tự động hóa sổ sách:** Liên kết trực tiếp thông tin vào file báo cáo tài chính hàng tháng.
