# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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



@pytest.fixture(scope="function")
def driver_con_login(driver):
    """Fixture que realiza el login y devuelve el driver posicionado en el inventario."""
    driver.get("https://www.saucedemo.com/")
    
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_TITLE = (By.CLASS_NAME, "title") 
    
    # Realizar el Login
    driver.find_element(*USERNAME_FIELD).send_keys("standard_user")
    driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")
    driver.find_element(*LOGIN_BUTTON).click()
    
    # Espera explícita para asegurar la carga del catálogo
    wait = WebDriverWait(driver, 10) 
    wait.until(EC.visibility_of_element_located(INVENTORY_TITLE))
    
    return driver