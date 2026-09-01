"""
Ülesanne 3 – Nuppudele klõpsamine.

- Avab Add/Remove Elements lehe.
- Vajutab "Add Element" nuppu 5 korda.
- Kustutab kõik lisatud elemendid ühe kaupa.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1)

    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    for _ in range(5):
        add_button.click()
        time.sleep(0.3)

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(f"Lisati {len(delete_buttons)} elementi.")

    while True:
        delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

        if not delete_buttons:
            break

        delete_buttons[0].click()
        time.sleep(0.3)

    print("Kõik lisatud elemendid kustutati.")

finally:
    driver.quit()
