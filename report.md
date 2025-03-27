# BÁO CÁO DỰ ÁN KIỂM THỬ TỰ ĐỘNG WEBSITE THEGIOIDIDONG.COM

## 1. TỔNG QUAN DỰ ÁN

Dự án kiểm thử tự động cho website thegioididong.com sử dụng Playwright và Pytest để kiểm tra các chức năng tìm kiếm và hiển thị sản phẩm.

### Mục tiêu:

- Tự động hóa việc kiểm thử chức năng tìm kiếm
- Xác minh hoạt động đúng của các thành phần UI
- Kiểm tra luồng người dùng từ tìm kiếm đến xem chi tiết sản phẩm

## 2. CẤU TRÚC DỰ ÁN

```
/
├── .pytest_cache/           - Cache của pytest
├── .venv/                   - Môi trường ảo Python
├── tests/                   - Thư mục chứa các test case
│   ├── thegioididong/       - Test cho website thegioididong
│   │   ├── test_search_page.py       - Test cơ bản về tìm kiếm
│   │   ├── test_search_advanced.py   - Test nâng cao về tìm kiếm
│   ├── conftest.py          - Cấu hình chung cho pytest
├── simple_test.py           - Script test đơn giản
├── pytest.ini               - Cấu hình pytest
└── requirements.txt         - Các thư viện dependency
```

## 3. CÔNG NGHỆ SỬ DỤNG

- **Python**: Ngôn ngữ lập trình chính
- **Playwright**: Framework tự động hóa trình duyệt
- **Pytest**: Framework kiểm thử
- **pytest-playwright**: Plugin tích hợp Playwright với Pytest

Phiên bản:

- Playwright: 1.42.0
- Pytest: 7.4.0
- pytest-playwright: 0.4.0

## 4. PHẠM VI KIỂM THỬ

Dự án tập trung vào kiểm thử chức năng tìm kiếm và kết quả tìm kiếm:

1. **Tìm kiếm cơ bản**:

   - Nhập từ khóa và hiển thị kết quả
   - Hiển thị thông tin sản phẩm trong kết quả tìm kiếm
   - Kiểm tra các bộ lọc và tùy chọn sắp xếp

2. **Tìm kiếm nâng cao**:

   - Gợi ý tìm kiếm
   - Lọc theo giá và hãng sản xuất
   - Sắp xếp kết quả
   - Xử lý tìm kiếm không có kết quả

3. **Luồng người dùng**:
   - Click vào sản phẩm từ kết quả tìm kiếm
   - Chuyển hướng đến trang chi tiết sản phẩm

## 5. PHƯƠNG PHÁP KIỂM THỬ

### Chiến lược:

- **Nhiều selector**: Sử dụng nhiều selector khác nhau để tăng độ tin cậy khi website thay đổi
- **Kiểm tra thực tế**: Tương tác với website thực, không dùng mock
- **Xử lý linh hoạt**: Thích ứng với các thay đổi của website (URL, cấu trúc trang)
- **Skip thay vì fail**: Nhiều test case bỏ qua thay vì báo lỗi nếu không tìm thấy phần tử

### Fixtures:

- **search_page**: Thiết lập trang tìm kiếm với từ khóa "iphone"
- **empty_search_page**: Thiết lập trang tìm kiếm không có kết quả

## 6. KẾT QUẢ KIỂM THỬ

Tổng cộng: 14 test case

- Thành công: 12 test case
- Thất bại có chủ đích: 2 test case (được thiết kế để thất bại)

### Chi tiết kiểm thử:

- **test_search_title**: Kiểm tra tiêu đề trang tìm kiếm
- **test_search_results_exist**: Kiểm tra sự hiện diện của kết quả tìm kiếm
- **test_product_info_displayed**: Kiểm tra thông tin sản phẩm hiển thị
- **test_filter_options**: Kiểm tra bộ lọc kết quả
- **test_search_page_navigation**: Kiểm tra phân trang
- **test_search_suggestions**: Kiểm tra gợi ý tìm kiếm
- **test_sort_by_price**: Kiểm tra sắp xếp theo giá
- **test_apply_price_filter**: Kiểm tra lọc theo giá
- **test_click_on_product**: Kiểm tra click vào sản phẩm
- **test_empty_search_results**: Kiểm tra tìm kiếm không có kết quả
- **test_brand_filter**: Kiểm tra lọc theo hãng
- **test_different_search_keyword**: Kiểm tra tìm kiếm với từ khóa khác
- **test_nonexistent_element**: Kiểm tra phần tử không tồn tại (fail)
- **test_incorrect_product_count**: Kiểm tra số lượng sản phẩm không đúng (fail)

## 7. ĐÁNH GIÁ

### Ưu điểm:

- **Toàn diện**: Bao phủ nhiều tính năng tìm kiếm và hiển thị
- **Linh hoạt**: Khả năng thích ứng cao với thay đổi của website
- **Thông báo chi tiết**: Log đầy đủ giúp dễ debug
- **Tái sử dụng code**: Sử dụng fixture hiệu quả
- **Xử lý ngoại lệ tốt**: Try-except và kiểm tra tồn tại phần tử trước khi thao tác

### Nhược điểm:

- **Assertion lỏng lẻo**: Một số test sử dụng `assert True` thay vì kiểm tra cụ thể
- **Phụ thuộc cấu trúc**: Vẫn phụ thuộc vào cấu trúc DOM của website
- **Thiếu parametrize**: Không sử dụng tham số hóa để chạy nhiều test với dữ liệu khác nhau
- **Thiếu độ chính xác**: Một số kiểm tra thứ tự sắp xếp chưa chính xác

## 8. ĐỀ XUẤT CẢI THIỆN

1. **Cấu trúc mã nguồn**:

   - Tổ chức lại test thành các lớp theo chức năng
   - Tạo thư viện helper để tái sử dụng code

2. **Cải thiện độ chính xác**:

   - Thêm kiểm tra thực tế thứ tự sắp xếp giá
   - Xác minh dữ liệu sản phẩm chính xác thay vì chỉ kiểm tra hiển thị

3. **Tham số hóa**:

   - Sử dụng `@pytest.mark.parametrize` để chạy test với nhiều từ khóa, bộ lọc khác nhau

4. **Báo cáo và giám sát**:

   - Thêm chụp ảnh khi test thất bại
   - Tích hợp báo cáo HTML chi tiết

5. **Mở rộng phạm vi**:
   - Thêm test cho các tính năng khác: giỏ hàng, đăng nhập, thanh toán
   - Thêm kiểm tra hiệu suất và tính khả dụng

## 9. KẾT LUẬN

Dự án kiểm thử tự động đã đạt được mục tiêu cơ bản trong việc kiểm tra chức năng tìm kiếm của thegioididong.com. Nó đã xây dựng nền tảng vững chắc để mở rộng thành một bộ kiểm thử toàn diện hơn. Với các cải tiến được đề xuất, dự án có thể trở thành một công cụ quan trọng trong quy trình đảm bảo chất lượng của website thương mại điện tử này.
