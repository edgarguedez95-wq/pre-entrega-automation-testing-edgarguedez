# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # Opciones de Chrome (opcional: ejecutar en modo headless para entornos CI/CD)
    # chrome_options = Options()
    # chrome_options.add_argument("--headless") 
    
    # Inicialización del WebDriver usando webdriver-manager
    # Esto descarga automáticamente el driver de Chrome.
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service) # Puedes añadir options=chrome_options si usas headless
    
    # Configuración del navegador
    web_driver.maximize_window()
    
    # El 'yield' devuelve la instancia de WebDriver a la función de prueba (test_login_exitoso)
    yield web_driver
    
    # La limpieza (cerrar el navegador) se ejecuta después de que la prueba termina
    web_driver.quit()