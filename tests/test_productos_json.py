# tests/test_productos_json.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_json_productos

# Cargamos los nombres de los productos desde el JSON
LISTA_PRODUCTOS = leer_json_productos("datos/productos.json")

@pytest.mark.parametrize("nombre_producto", LISTA_PRODUCTOS)
def test_agregar_producto_desde_json(driver, nombre_producto):
    """Test parametrizado que valida la adición de productos al carrito usando datos de un JSON"""
    
    # 1. Realizar login previo para acceder al inventario
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    
    # 2. Instanciar la página de inventario
    inventory_page = InventoryPage(driver)
    
    # 3. Buscar y agregar el producto parametrizado
    inventory_page.agregar_producto_por_nombre(nombre_producto)
    
    # 4. Validar que el carrito refleje el cambio
    assert inventory_page.obtener_cantidad_carrito() == "1", f"El producto {nombre_producto} no se pudo agregar al carrito"
    print(f"✅ Producto validado y agregado con éxito: {nombre_producto}")