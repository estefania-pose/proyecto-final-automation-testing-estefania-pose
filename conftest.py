import os
import pathlib
import tempfile
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCREEN_DIR = pathlib.Path('reports/screens')
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    
    # Crea un directorio temporal único para que Chrome nazca 100% limpio y sin historial
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_dir}")
    
    # Apaga los servicios de contraseñas y alertas de seguridad
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,SafeBrowsingEnhancedProtection")
    options.add_argument("--disable-save-password-bubble")
    
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def pytest_html_results_table_header(cells):
    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, getattr(report, 'page_url', '-'))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        driver = item.funcargs.get('driver')
        if driver:
            report.page_url = driver.current_url
            if report.failed:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                safe_name = item.name.replace("[", "_").replace("]", "_")
                file_path = SCREEN_DIR / f"{safe_name}_{timestamp}.png"
                driver.save_screenshot(str(file_path))
                
                if hasattr(report, 'extra'):
                    report.extra.append({
                        'name': 'screenshot',
                        'format': 'image',
                        'content': str(file_path)
                    })
        