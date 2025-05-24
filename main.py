import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Настройка браузера под CI (GitHub Actions) + suppress logs
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--user-data-dir=/tmp/unique-profile')
options.add_argument('--log-level=3')  # Подавление лишних логов

# Инициализация WebDriver с опциями
driver = webdriver.Chrome(options=options)

try:
    # 1) Открываем сайт NASA
    driver.get("https://eyes.nasa.gov/apps/solar-system/")
    time.sleep(5)  # Ждём загрузки визуализаций

    # 2) Проверка заголовка
    assert "Solar System" in driver.title

    # 3) Сохранение успешного скриншота
    driver.save_screenshot("1_homepage.png")

    print("Тест пройден успешно.")

except Exception as e:
    print("Ошибка в тесте:", e)
    driver.save_screenshot("error.png")

finally:
    driver.quit()
