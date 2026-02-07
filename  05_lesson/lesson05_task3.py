from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


gecko_driver_path = r'C:\\Users\\Елена\\Downloads\\geckodriver-v0.36.0-win64\\geckodriver.exe'


options = webdriver.FirefoxOptions()

service = Service(gecko_driver_path)

driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get('http://the-internet.herokuapp.com/inputs')
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, 'input')

    input_field.send_keys('Sky')
    time.sleep(2)

    input_field.clear()
    time.sleep(2)

    input_field.send_keys('Pro')
    time.sleep(2)

finally:
    driver.quit()















