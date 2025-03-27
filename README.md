# Test Automation cho Thegioididong.com

Dự án test automation đơn giản cho website thegioididong.com sử dụng Playwright và Python.

## Cài đặt

1. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

2. Cài đặt trình duyệt cho Playwright:

```bash
playwright install
```

## Chạy test

### Cách 1: Chạy test đơn giản

Chạy file test đơn giản (khuyên dùng cho người mới bắt đầu):

```bash
python simple_test.py
```

### Cách 2: Chạy test với pytest

```bash
# Chạy tất cả các test
pytest

# Chạy test cụ thể
pytest tests/thegioididong/test_homepage.py

# Chạy test cụ thể với hiển thị trình duyệt
pytest tests/thegioididong/test_homepage.py --headed
```

## Lưu ý

- Nếu gặp lỗi, hãy kiểm tra selectors có phù hợp với cấu trúc hiện tại của trang web không
- Thời gian timeout được thiết lập khá dài (60s) để đảm bảo trang web có đủ thời gian tải
- File `simple_test.py` là file đơn giản nhất để kiểm tra Playwright đã hoạt động đúng chưa
