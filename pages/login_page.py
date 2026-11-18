# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 1. Identidad de la página (URL)
    URL = "https://www.saucedemo.com/"

    # 2. Locators privados y centralizados
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # 3. Constructor (Inyección del driver)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 4. Métodos de navegación y acción
    def abrir(self):
        """Carga la URL de login en el navegador."""
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario: str):
        """Escribe el nombre de usuario."""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_clave(self, clave: str):
        """Escribe la contraseña."""
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self

    def hacer_clic_login(self):
        """Hace clic en el botón Login."""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self, usuario, clave):
        """Método de conveniencia para hacer login completo."""
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        return self

    # 5. Métodos de verificación
    def esta_error_visible(self) -> bool:
        """Comprueba si aparece un mensaje de error en la página tras un intento fallido."""
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False