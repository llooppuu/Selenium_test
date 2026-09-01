"""
Ülesanne 4 – Vormitäitmine.

- Avab sisselogimislehe.
- Sisestab kasutajanime ja parooli.
- Vajutab Login.
- Kontrollib, kas sisselogimine õnnestus.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login_button.click()

    time.sleep(2)

    flash_message = driver.find_element(By.ID, "flash").text

    if "You logged into a secure area!" in flash_message:
        print("TEST ÕNNESTUS: sisselogimine õnnestus.")
    else:
        print("TEST EBAÕNNESTUS: oodatud teadet ei leitud.")
        print("Lehel kuvati:", flash_message)

finally:
    driver.quit()
