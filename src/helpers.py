# conftest.py (en la carpeta tests/ o en la raíz)
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Inicialización del WebDriver (ej. Chrome)
    # Usa WebDriver Manager para simplificar la gestión del driver
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    
    # Configuración básica (ej. maximizar la ventana)
    web_driver.maximize_window()
    
    # Devuelve la instancia del driver a la prueba
    yield web_driver
    
    # Limpieza: Cierra el navegador después de que la prueba termine
    web_driver.quit()