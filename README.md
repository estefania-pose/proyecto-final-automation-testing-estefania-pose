# Framework de Automatización de Pruebas (UI + API + BDD)

Proyecto Final Integrador desarrollado en Python aplicando el patrón **Page Object Model (POM)**, pruebas parametrizadas *Data-Driven* (CSV/JSON), automatización de APIs REST, escenarios BDD con Gherkin y ejecución continua mediante GitHub Actions.

## 🚀 Tecnologías Utilizadas
* **Python 3.12+**
* **Pytest & pytest-html**: Orquestación de pruebas y generación de reportes visuales autocontenidos.
* **Selenium WebDriver**: Automatización de pruebas de interfaz web sobre [SauceDemo](https://www.saucedemo.com/).
* **Requests & Faker**: Validación de endpoints REST sobre [JSONPlaceholder](https://jsonplaceholder.typicode.com/) con datos dinámicos.
* **Behave**: Pruebas de comportamiento (BDD) escritas en lenguaje Gherkin.
* **GitHub Actions**: Integración Continua (CI) con generación automática de artefactos.

## 📁 Estructura del Proyecto
* `pages/`: Clases Page Object (`LoginPage`, `InventoryPage`) que encapsulan selectores y acciones.
* `tests/`: Pruebas UI parametrizadas desde archivos externos (`datos/login.csv` y `datos/productos.json`).
* `tests_api/`: Pruebas de API cubriendo métodos `GET`, `POST`, `PUT`, `PATCH` y `DELETE`.
* `features/`: Historias en Gherkin (`.feature`), conectores (`steps/`) y hooks globales (`environment.py`).
* `utils/`: Utilidades para lectura de datos (`datos.py`) y registro centralizado (`logger.py`).
* `reports/` y `logs/`: Evidencias de ejecución, capturas automáticas ante fallos y logs cronológicos.

## ⚙️ Instalación y Ejecución Local
1. Clonar el repositorio e instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar la suite completa (UI + API + BDD). Genera el reporte en `reports/report.html`:
   ```bash
   pytest
   ```
3. Ejecutar solo una parte de la suite:
   ```bash
   pytest tests/                  # UI (Selenium)
   pytest tests_api/              # API REST
   pytest -m smoke                # solo pruebas críticas
   pytest -m "api and not e2e"    # combinando marcadores
   behave                         # escenarios BDD directamente con Behave
   ```

> **Requisito:** tener Google Chrome instalado (Selenium Manager descarga el driver automáticamente).
> En CI (`CI=true`) el navegador corre en modo *headless*.

## 🥒 Cómo se integra BDD con Pytest
`tests_behave/test_behave_suite.py` ejecuta Behave como un subproceso desde un único test de pytest.
Por eso, en el reporte de pytest los escenarios BDD aparecen agrupados en **un solo resultado**
(`test_ejecutar_suite_bdd`). El detalle por escenario se ve en la salida de consola de Behave
y en `reports/behave.json`.

## 📊 Evidencias generadas
* `reports/report.html`: reporte HTML autocontenido de pytest.
* `reports/screens/`: capturas automáticas ante cada fallo (UI y BDD).
* `reports/behave.json`: resultado detallado de los escenarios Gherkin.
* `logs/`: logs cronológicos de la ejecución.
* En GitHub Actions todo se publica como artefacto `reportes-y-evidencias`.
