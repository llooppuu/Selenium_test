from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

SEARCH_QUERY = "Lauri"


def accept_google_cookies(driver):
    possible_buttons = [
        (By.ID, "L2AGLb"),
        (By.XPATH, "//button//*[contains(text(), 'Nõustu kõigiga')]/.."),
        (By.XPATH, "//button//*[contains(text(), 'Accept all')]/.."),
        (By.XPATH, "//button//*[contains(text(), 'Reject all')]/.."),
    ]

    for by, value in possible_buttons:
        try:
            driver.find_element(by, value).click()
            time.sleep(1)
            return
        except NoSuchElementException:
            pass


def main():
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        # Ava Google
        driver.get("https://www.google.com")
        time.sleep(2)

        accept_google_cookies(driver)

        # Leia Google'i otsingukast nime "q" järgi
        search_box = driver.find_element(By.NAME, "q")

        # Sisesta otsingupäring ja käivita otsing
        search_box.send_keys(SEARCH_QUERY)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)
        print(f'Otsing "{SEARCH_QUERY}" käivitati edukalt.')

        input("Vajuta Enter, et programm lõpetada...")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
