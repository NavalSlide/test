import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Configuración para evitar detección y modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")  # Necesario para entornos como GitHub Actions
chrome_options.add_argument("--disable-dev-shm-usage")  # Evitar problemas de memoria en contenedores
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--mute-audio")  # Silenciar el video
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# El ChromeDriver se instalará automáticamente en GitHub Actions
driver = webdriver.Chrome(options=chrome_options)

def watch_video(link, views, min_time, max_time):
    driver.get(link)
    time.sleep(5)  # Esperar que cargue el video
    
    for i in range(views):
        watch_time = random.randint(min_time, max_time)
        print(f"[INFO] Viendo video {i + 1}/{views} por {watch_time} segundos...")
        time.sleep(watch_time)
        
        # Simular interacción humana (mover mouse y hacer clic en pantalla)
        actions = ActionChains(driver)
        actions.move_by_offset(random.randint(100, 500), random.randint(100, 500)).perform()
        actions.click().perform()
        
        # Refrescar la página para contar otra vista
        driver.refresh()
        time.sleep(random.randint(2, 5))  # Espera aleatoria antes de la siguiente vista
    
    driver.quit()

# Configuración
link = "https://www.youtube.com/watch?v=zVAnXmQOisc&t=16s&ab_channel=Pardo18"  # Enlace del video
views = 50  # Número de vistas
min_time = 30  # Tiempo mínimo viendo el video (segundos)
max_time = 60  # Tiempo máximo viendo el video (segundos)

if __name__ == "__main__":
    watch_video(link, views, min_time, max_time)