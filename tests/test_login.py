import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# NOTA: Este test asume que tienes un 'fixture' llamado 'driver' configurado 
# en un archivo conftest.py para iniciar y cerrar el navegador.

def test_login_exitoso(driver):
    """
    Objetivo: Automatizar el login exitoso en saucedemo.com y validar la página de inventario.
    Criterios: Login con espera explícita y validación de URL e H1.
    """
    
    # 1. Navegar a la página de login de saucedemo.com
    driver.get("https://www.saucedemo.com/")
    
    # --- Localizadores de elementos ---
    
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    # Ingresar credenciales válidas
    driver.find_element(*USERNAME_FIELD).send_keys("standard_user")
    driver.find_element(*PASSWORD_FIELD).send_keys("secret_sauce")
    
    # Hacer click en el botón de Login
    driver.find_element(*LOGIN_BUTTON).click()
    
    # --- Espera Explícita y Validación de la página de Inventario ---
    
    # Localizador para el título "Products" (o "Swag Labs" según el requerimiento, 
    # pero el texto real en la página es "Products")
    INVENTORY_TITLE = (By.CLASS_NAME, "title") 
    
    # Definir la espera explícita
    wait = WebDriverWait(driver, 10) # Espera máxima de 10 segundos
    
    # Esperar hasta que el elemento del título sea VISIBLE en la nueva página.
    products_title_element = wait.until(
        EC.visibility_of_element_located(INVENTORY_TITLE)
    )
    
    # 1. Validar la URL (criterio: "/inventory.html")
    current_url = driver.current_url
    assert "/inventory.html" in current_url, \
        f"Error: No se redirigió a /inventory.html. URL actual: {current_url}"
    
    # 2. Validar el texto del encabezado (criterio: "Products" / "Swag Labs")
    expected_title_text = "Products" 
    actual_title_text = products_title_element.text
    
    assert actual_title_text == expected_title_text, \
        f"Error: Título incorrecto. Esperado: '{expected_title_text}', Actual: '{actual_title_text}'"