from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r'C:\\Users\\Елена\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

options = webdriver.ChromeOptions()

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)

try:

    driver.get('http://uitestingplayground.com/dynamicid')

    time.sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

    time.sleep(3)

finally:
    driver.quit()
