# tests/test_login.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver):
    """Prueba que un usuario válido pueda iniciar sesión correctamente usando POM."""
    # 1. Instanciar la página de login y abrirla
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # 2. Realizar el login completo
    login_page.login_completo("standard_user", "secret_sauce")
    
    # 3. Verificar que llegamos a la página de inventario
    inventory_page = InventoryPage(driver)
    titulo = inventory_page.obtener_titulo()
    
    assert titulo == "Products", f"Se esperaba el título 'Products', pero se obtuvo '{titulo}'"
    print("✅ ¡Test de Login con POM ejecutado y verificado con éxito!")