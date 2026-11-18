from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITULO_PAGINA = (By.CLASS_NAME, "title")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self._TITULO_PAGINA)).text

    def agregar_producto_por_nombre(self, nombre_producto: str):
        items = self.wait.until(EC.presence_of_all_elements_located(self._INVENTORY_ITEMS))
        for item in items:
            titulo = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if titulo == nombre_producto:
                item.find_element(By.TAG_NAME, "button").click()
                return self
        raise ValueError(f"Producto '{nombre_producto}' no encontrado en el inventario.")

    def obtener_cantidad_carrito(self) -> str:
        badges = self.driver.find_elements(*self._CART_BADGE)
        return badges[0].text if badges else "0"