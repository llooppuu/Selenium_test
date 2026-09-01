"""
Ülesanne 5 – Navigatsioon.

- Avab The Internet avalehe.
- Klõpsab lingil "Checkboxes".
- Märgib mõlemad checkbox'id.
- Läheb Seleniumi abil eelmisele lehele tagasi.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(1)

    checkboxes_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
    checkboxes_link.click()
    time.sleep(1)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

    print("Mõlemad checkbox'id on märgitud.")

    time.sleep(1)
    driver.back()
    time.sleep(1)

    print("Liiguti tagasi eelmisele lehele.")
    print("Praegune URL:", driver.current_url)

finally:
    driver.quit()
