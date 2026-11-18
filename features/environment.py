import os
import pathlib
import tempfile
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCREEN_DIR = pathlib.Path('reports/screens')
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

def before_all(context):
    options = Options()
    
    # Directorio temporal único para Behave
    context.temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={context.temp_dir}")
    
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
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")

def after_step(context, step):
    if step.status == 'failed' and hasattr(context, 'driver'):
        timestamp = datetime.now().strftime('%H%M%S')
        safe_name = step.name.replace(" ", "_")[:30]
        file_path = SCREEN_DIR / f"bdd_{safe_name}_{timestamp}.png"
        context.driver.save_screenshot(str(file_path))

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()