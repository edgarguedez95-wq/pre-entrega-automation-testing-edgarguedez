## Propósito del Proyecto (Objetivo)

El objetivo de este proyecto es aplicar los conocimientos de automatización de pruebas adquiridos, utilizando Python y Selenium WebDriver. Automatiza flujos funcionales críticos en el sitio de prueba saucedemo.com.

## Tecnologías utilizadas

Tecnología,Propósito
Lenguaje,Python 3.x
Framework de Pruebas,[Pytest]
Automatización Web,[Selenium WebDriver]
Generación de Reportes,[pytest-html]
Gestión de Drivers,[WebDriver-Manager]

## Los Casos de Prueba implementados son:

- Login Exitoso: Navegación e inicio de sesión con credenciales válidas (standard_user/secret_sauce).
- Verificación del Catálogo: Validación de la presencia de productos y elementos de la interfaz.
- Interacción con Carrito: Adición de un producto y verificación de su presencia en el carrito.

## Instrucciones de Instalación de Dependencias

## 4. Instrucciones de Instalación de Dependencias

Para ejecutar las pruebas localmente, es necesario clonar el repositorio e instalar las dependencias.

1.  **Clonar el Repositorio:**
    bash
    git clone [https://github.com/edgarguedez95-wq/pre-entrega-automation-testing-edgarguedez.git](https://github.com/edgarguedez95-wq/pre-entrega-automation-testing-edgarguedez.git)
    cd pre-entrega-automation-testing-edgarguedez

2.  **Crear y Activar el Entorno Virtual (`venv`):**
    bash

    # Crear el entorno virtual:

    python -m venv venv

    # Para activar, usar el comando según la terminal de Windows:

    # -----------------------------------------------------------

    # En PowerShell:

    # .\venv\Scripts\Activate

    # -----------------------------------------------------------

    # En Símbolo del Sistema (CMD):

    # venv\Scripts\activate

3.  **Instalar las Dependencias:**
    bash
    pip install -r requirements.txt

## Comando para Ejecutar las Pruebas y Generar Reporte HTML

pytest tests/ -v --html=reports/reporte.html --self-contained-html
