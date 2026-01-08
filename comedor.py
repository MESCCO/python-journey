import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO

# ----------------------------------------
# CONFIGURACIÓN
# ----------------------------------------
URL = "http://bienestar.unsaac.edu.pe/"  # <-- pon aquí la URL exacta de la reserva
CHROME_PATH = "chromedriver.exe"         # ruta a tu chromedriver

CODIGO_ESTUDIANTE = "246197"             # <-- tu código UNSAAC
CLAVE_VAUCHER = "20526"                  # <-- clave de 5 dígitos del voucher
# ----------------------------------------

# Inicializar navegador
driver = webdriver.Chrome()
driver.get(URL)

time.sleep(1)

# Completar CÓDIGO
driver.find_element(By.NAME, "codigo").send_keys(CODIGO_ESTUDIANTE)

# Completar CLAVE
driver.find_element(By.NAME, "clave").send_keys(CLAVE_VAUCHER)

# ----------------------------------------
# OBTENER LA IMAGEN DEL CAPTCHA
# ----------------------------------------

# Buscar elemento <img> del captcha
captcha_img = driver.find_element(By.XPATH, "//img[contains(@src,'captcha')]")

# Obtener URL real de la imagen
captcha_url = captcha_img.get_attribute("src")

# Descargar imagen
r = requests.get(captcha_url)
img = Image.open(BytesIO(r.content))

# Mostrar captcha para que lo leas
img.show()

# Pedir al usuario el texto que ve
captcha_text = input("\nIngresa el CAPTCHA tal como aparece: ")

# ----------------------------------------
# INGRESAR CAPTCHA Y ENVIAR FORMULARIO
# ----------------------------------------

# Campo del captcha
campo_captcha = driver.find_element(By.NAME, "captcha")
campo_captcha.send_keys(captcha_text)

# Botón enviar (puede cambiar ID dependiendo de la página)
boton = driver.find_element(By.XPATH, "//input[@type='submit' or @value='Reservar']")
boton.click()

print("\n✔ Formulario enviado correctamente.")
