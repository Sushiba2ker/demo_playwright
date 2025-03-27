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

### Cách 1: Chạy test với auto (Không custom được số lượng cửa sổ browser)

```bash
python -m pytest -v -n auto
```

### Cách 2: Chạy test với custom số lượng cửa sổ browser

```bash
# Có thể thay số lượng số cửa sổ mong muốn
python -m pytest -v -n 4

# Chạy test cụ thể
pytest tests/thegioididong/test_search_advanced.py

# Chạy test cụ thể với hiển thị trình duyệt
pytest tests/thegioididong/test_search_page.py --headed
```

## Lưu ý

- Nếu gặp lỗi, hãy kiểm tra selectors có phù hợp với cấu trúc hiện tại của trang web không
- Thời gian timeout được thiết lập khá dài (60s) để đảm bảo trang web có đủ thời gian tải
