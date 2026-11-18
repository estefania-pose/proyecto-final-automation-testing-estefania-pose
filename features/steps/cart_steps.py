from behave import when, then
from pages.inventory_page import InventoryPage
from utils.logger import logger

@when('agrego el producto "{producto}" al carrito')
def step_agregar_producto(context, producto):
    logger.info(f"BDD: Agregando producto '{producto}'")
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.agregar_producto_por_nombre(producto)

@then('el contador del carrito muestra "{cantidad}"')
def step_validar_contador(context, cantidad):
    assert context.inventory_page.obtener_cantidad_carrito() == cantidad