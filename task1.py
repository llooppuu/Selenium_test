from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SEARCH_QUERY = "Lauri"

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)


driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.google.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(SEARCH_QUERY)
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)

    screenshot_path = SCREENSHOT_DIR / "pilt.png"
    driver.save_screenshot(str(screenshot_path))

    print(f'Otsing "{SEARCH_QUERY}" tehtud.')
    print(f"Screenshot salvestatud: {screenshot_path}")

finally:
    driver.quit()
