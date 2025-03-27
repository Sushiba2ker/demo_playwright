import pytest
from playwright.sync_api import Playwright, Page
import os
import datetime

# Đảm bảo thư mục screenshots tồn tại
screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
os.makedirs(screenshots_dir, exist_ok=True)

@pytest.fixture(scope="function")
def page(playwright: Playwright, request) -> Page:
    """Fixture chuẩn bị browser và trang"""
    # Khởi chạy browser
    browser = playwright.chromium.launch(headless=False)
    
    # Tạo context mới
    context = browser.new_context()
    
    # Tạo page mới
    page = context.new_page()
    
    # Thiết lập timeout dài hơn
    page.set_default_timeout(60000)
    
    # Chuyển đến trang web
    page.goto("https://www.thegioididong.com")
    
    # Trả về page để sử dụng trong test
    yield page
    
    # Chụp ảnh màn hình sau mỗi test (thành công và thất bại)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = request.node.name
    screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    page.screenshot(path=screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")
    
    # Đóng browser sau khi test hoàn thành
    context.close()
    browser.close()

# Hook để chụp ảnh khi test thất bại
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # Chỉ quan tâm đến thất bại trong giai đoạn call
    if rep.when == "call" and rep.failed:
        try:
            # Lấy page từ fixture
            page = item.funcargs.get("page")
            if page is not None:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(screenshots_dir, f"FAIL_{item.name}_{timestamp}.png")
                page.screenshot(path=screenshot_path)
                print(f"Failure screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Failed to capture screenshot on test failure: {e}") 