from behave import given, when, then
from pages.login_page import LoginPage
from utils.logger import logger

@given('estoy en la pagina de login de SauceDemo')
def step_abrir_login(context):
    logger.info("BDD: Abriendo pagina de login")
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()

@when('ingreso usuario "{usuario}" y contrasena "{clave}"')
def step_ingresar_credenciales(context, usuario, clave):
    clave_real = clave if clave else ""
    logger.info(f"BDD: Intentando login con usuario '{usuario}'")
    context.login_page.login_completo(usuario, clave_real)

@then('ingreso correctamente al inventario')
def step_validar_inventario(context):
    assert "inventory.html" in context.driver.current_url

@then('visualizo un mensaje de error en pantalla')
def step_validar_error(context):
    assert context.login_page.esta_error_visible()