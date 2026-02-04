from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

gecko_driver_path = r'C:\\Users\\Елена\\Downloads\\geckodriver-v0.36.0-win64\\geckodriver.exe'

options = webdriver.FirefoxOptions()

service = Service(gecko_driver_path)

driver = webdriver.Firefox(service=service, options=options)

try:

    driver.get('http://the-internet.herokuapp.com/login')
    time.sleep(2)

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('tomsmith')
    time.sleep(2)


    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('SuperSecretPassword!')
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(5)


    success_message = driver.find_element(By.CLASS_NAME, 'flash.success').text.strip()
    print(success_message)

finally:
    driver.quit()
