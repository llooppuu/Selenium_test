from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    driver.get("https://quotes.toscrape.com")
    time.sleep(2)

    quote_blocks = driver.find_elements(By.CLASS_NAME, "quote")

    print(f"Leiti {len(quote_blocks)} tsitaati.\n")

    for i, block in enumerate(quote_blocks, start=1):
        text = block.find_element(By.CLASS_NAME, "text").text
        author = block.find_element(By.CLASS_NAME, "author").text
        print(f"{i}. {text}")
        print(f"   Autor: {author}\n")

finally:
    driver.quit()
