import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Настройка браузера в headless-режиме 
options = Options()
options.add_argument("--headless")            
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Инициализация драйвера 
driver = webdriver.Chrome()

try:
    # 1) Открываем сайт
    driver.get("https://eyes.nasa.gov/apps/solar-system/")
    time.sleep(5)  

    # 2) Проверяем заголовок страницы
    assert "Solar System" in driver.title

    # 3) Делаем скриншот главной страницы
    driver.save_screenshot("1_homepage.png")
    
    time.sleep(1)
   
    print("Тест пройден успешно.")
except Exception as e:
    print("Ошибка в тесте:", e)
    driver.save_screenshot("error.png")
finally:
    driver.quit()
