# 🌐 Hướng Dẫn Kích Hoạt (Demo Usecase): Web Portal (Cổng Thông Tin)

> **Tình Huống Sử Dụng (Usecase): Ra Mắt "Sổ Tay Nhân Viên" Dạng Website**
> Dành cho khối Hành Chính/Nhân Sự (HR). Hệ thống này giúp bạn biến những thư mục chứa đầy Nội quy, Danh bạ, Quy chế thưởng phạt đang nằm rải rác trên máy tính hoặc ổ cứng thành một "Cổng thông tin chuyên nghiệp" (Website). Toàn công ty có thể tra cứu nhanh qua điện thoại mọi lúc mọi nơi thông qua một Đường Link truy cập miễn phí!

---

## 🎯 Bối Cảnh Thực Tiễn & Logic Hoạt Động
**Mục tiêu:** Bạn không thể cứ in giấy hay bắt nhân viên phải tải tài liệu PDF cồng kềnh mỗi khu vực. Hãy đưa mọi thứ lên chung một Portal (Trang chủ nội bộ).

**Giải pháp với AI Agent (3 Pha tự động):**
- **Pha 1 (Chuyển Hóa Dữ Liệu):** Bạn chỉ việc ném file (.txt, .csv) vào một thư mục cho sẵn. AI Agent sẽ tự động nén tất cả các file đó thành mã lệnh (Code) và thiết kế một giao diện Web tuyệt đẹp phủ lớp màu thông minh.
- **Pha 2 (Đồng Bộ Kho):** Agent tự động mở một nhà kho trên Đám mây (Github) riêng để bảo quản trang Web đó.
- **Pha 3 (Phát Sóng):** Chỉ mất 10 giây để bạn nhấp một nút trên Vercel, trạm này sẽ kích hoạt và phóng Website nội bộ của bạn lên Internet toàn cầu rực rỡ!

*(Lưu ý: Đảm bảo bạn đã cái đặt hạ tầng ở `SETUP_GUIDE.md` thành công trước khi áp dụng hệ thống chạy thực tiễn này)*

---

## 🛠 Chuẩn Bị File Đầu Vào (Mockup Data)
Để luyện tập tình huống này, chúng tôi đã chuẩn bị sẵn cho bạn một thư mục "Kho Dữ Liệu" ở ngay tại dự án tên là: **`Raw_Documents`**.
Bên trong thư mục này chứa đầy đủ thông tin giả định cho một Cổng thông tin quy chuẩn của Doanh nghiệp:
1. `Danh_Ba_Nhan_Vien.csv`: Khối file cấu trúc về số liên lạc nội bộ.
2. `Chinh_Sach_Thuong_Tet.txt` / `Noi_Quy_Cong_Ty.txt` / `Hdsd_Nghi_Phep.txt`: Khối file định dạng văn bản (Quy định cơ quan).

*Nhiệm vụ của bạn chỉ là đảm bảo toàn bộ file muốn lên mạng phải nằm trọn vẹn trong Folder `Raw_Documents`.*

---

## 🚀 Kích Hoạt Luồng AI (Execute 3 Pha)

Tiến hành vận hành bộ khung Agent hóa tự động. Hãy gọi lệnh ngay trong cửa sổ chat IDE.

### Pha 1: Nhào Nặn Giao Diện Portal Bởi Trí Tuệ Nhân Tạo
Gõ dòng câu thần chú này vào Chat:
```bash
/build-portal
```
*(Kết quả: Lệnh này kích hoạt nén mọi dữ liệu trong thư mục `Raw_Documents`. Màn hình sẽ văng ra một câu lệnh yêu cầu bạn mượn tay thao tác Prompt vào hộp Chat của Antigravity AI bên tay phải, để AI tự Code bộ khung Giao diện thiết kế cho trang web. Bạn hoàn toàn không cần động tay vào một dòng Code nào).*

### Pha 2: Tiễn Mã Nguồn Lên Kho Github (Đồng Bộ)
Ngay sau khi AI sản xuất xong Giao Diện thiết kế Web cực xịn, bạn phải tiến hành dọn nó cất kho. Mỗi dự án Portal cần một "Nhà Kho" riêng rẽ. 
Bạn hãy ra lệnh cho Agent đẩy mã nguồn lên Github kèm theo **Tên Nhà Kho** và phải ghi rõ là kho **TẠO MỚI** hay kho cũ cần **CẬP NHẬT**.

Ví dụ (Để học viên luyện tập tạo trang Nhân Sự mới):
```bash
/deploy-portal Hãy tạo mới kho lưu trữ tên là "so-tay-nhan-vien-2026" và đẩy code lên đó.
```
*(Ngay sau khi hoàn thành, Agent TỰ ĐỘNG tạo ra file bằng thẻ lưu trú `DEPLOY_REPORT.md` chứa thông tin chuẩn trích xuất URL liên kết cho bạn).*

### Pha 3: Triển Khai Phát Sóng Thành Đường Link Tại VERCEL
1. Vừa cầm thông tin `DEPLOY_REPORT.md`, bạn vừa lên ngay trình duyệt mở cổng Hosting Vercel. Nhìn góc phải bấm nút Đen: **Add New** -> Chọn **Project**.
2. Ở mục "Import Git Repository", nhãn quang của bạn sẽ thấy ngay tên kho `so-tay-nhan-vien-2026` lỳ lợm chờ sẵn. Bấm nút **Import**.
3. Tại giao diện Deploy kế tiếp, kéo xuống góc dưới cùng, nhấn **DEPLOY**. Hệ thống sẽ load từ 7-10 giây để phóng Web lên không gian đám mây.

**🎉 Thành Quả:** Bạn sẽ thấy pháo hoa rải ngập Web, một dòng URL xịn xò có định dạng `<tên_portal>.vercel.app` đã sẵn sàng! Gửi đường Link này qua Group Zalo Công ty và chờ đợi lời khen xuýt xoa của từng nhân viên!
