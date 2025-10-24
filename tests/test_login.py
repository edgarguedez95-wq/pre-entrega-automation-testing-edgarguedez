import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# NOTA: Este test asume que tienes un 'fixture' llamado 'driver' configurado 
# en un archivo conftest.py para iniciar y cerrar el navegador.

def test_login_exitoso(driver):
    """
    PRUEBA DE REQUERIMIENTO 1: Login en Sauce Demo.
    Criterios: Login automatizado, espera explícita, y validación de URL/Título (Products).
    Desarrollado por Edgar Guedez para la Pre-Entrega de QA.
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
    



# ----------------------------------------------------------------------------------

def test_verificar_catalogo(driver_con_login):
    """
    Caso de Prueba de Navegación:
    - Verifica título, presencia de productos, y lista nombre/precio del primero.
    """
    driver = driver_con_login  # Usamos el driver ya logueado desde el fixture
    
    # Localizadores clave del catálogo
    INVENTORY_HEADER = (By.CLASS_NAME, "title")
    PRODUCT_CONTAINERS = (By.CLASS_NAME, "inventory_item")
    
    # 1. Criterio: Valida título
    expected_title_text = "Products"
    actual_title_text = driver.find_element(*INVENTORY_HEADER).text
    assert actual_title_text == expected_title_text, f"Fallo en título. Actual: '{actual_title_text}'"

    # 2. Criterio: Valida presencia de productos 
    products = driver.find_elements(*PRODUCT_CONTAINERS)
    assert len(products) > 0, "No se encontraron productos en el catálogo."
    
    # 3. Criterio: Lista nombre/precio del primero.
    if products:
        first_product = products[0]
        PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
        PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
        
        nombre = first_product.find_element(*PRODUCT_NAME).text
        precio = first_product.find_element(*PRODUCT_PRICE).text
        
        print(f"\n[INFO] Primer Producto: Nombre='{nombre}', Precio='{precio}'")
        
        assert nombre != "", "El nombre del primer producto está vacío."
        assert precio.startswith("$"), "El precio del primer producto no tiene el símbolo '$'."





# ----------------------------------------------------------------------------------

def test_interaccion_carrito(driver_con_login):
    """
    Caso de Prueba de Carrito:
    - Agrega el primer producto disponible.
    - Verifica el contador del carrito.
    - Navega al carrito y verifica la presencia del ítem.
    """
    driver = driver_con_login  # Driver ya logueado
    
    # 1. Localizadores
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child .btn_primary")
    # Este localizador .inventory_item:first-child busca el primer producto
    # y luego busca el botón primario de "Add to cart" dentro de él.
    
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    
    # 2. Acciones: Añadir producto y verificar contador
    
    # Obtener el nombre del producto antes de añadirlo (para validación futura)
    product_name_element = driver.find_element(By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name")
    product_name = product_name_element.text
    
    # Criterio: Agrega primer producto
    driver.find_element(*ADD_TO_CART_BUTTON).click()
    
    # Criterio: Verificar que el contador del carrito se incremente
    cart_count = driver.find_element(*SHOPPING_CART_BADGE).text
    assert cart_count == "1", f"El contador del carrito no es '1', es '{cart_count}'"
    
    # 3. Navegar al carrito
    driver.find_element(*SHOPPING_CART_LINK).click()
    
    # 4. Validaciones en la página del carrito
    
    # Espera explícita para la carga del carrito
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(CART_ITEM))
    
    # Criterio: Verifica ítem en carrito (Comprobar que el producto añadido aparezca)
    cart_item_name_element = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    
    assert cart_item_name_element.text == product_name, "El nombre del producto en el carrito no coincide con el añadido."
    assert driver.find_element(*CART_ITEM).is_displayed(), "El producto no es visible en el carrito."