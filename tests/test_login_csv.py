# tests/test_login_csv.py
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

# Cargamos los datos usando nuestra función lectora de utils/datos.py
CASOS_LOGIN = leer_csv_login("datos/login.csv")

@pytest.mark.parametrize("usuario, clave, debe_funcionar", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar):
    """Test parametrizado que verifica el login leyendo credenciales desde un CSV"""
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Completar credenciales y enviar
    login_page.login_completo(usuario, clave)
    
    if debe_funcionar:
        # Si el usuario es válido, validamos que entramos al inventario
        assert "inventory.html" in driver.current_url, f"El usuario {usuario} debería haber ingresado con éxito"
        print(f"✅ Login exitoso como se esperaba para: {usuario}")
    else:
        # Si el usuario no debe funcionar (bloqueado o malo), verificamos que muestre error
        assert login_page.esta_error_visible(), f"El usuario {usuario} debería mostrar un error"
        print(f"✅ Error detectado correctamente para el usuario inválido/bloqueado: {usuario}")