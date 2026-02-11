from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


firefox_driver_path = r'C:\\Users\\Елена\\Downloads\\geckodriver-v0.36.0-win64\\geckodriver.exe'
service = Service(firefox_driver_path)
driver = webdriver.Firefox(service=service)

try:

    driver.get("http://uitestingplayground.com/ajax")


    blue_button = driver.find_element(By.XPATH, "//button[@id='ajaxButton']")
    blue_button.click()

    wait = WebDriverWait(driver, 15)
    green_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))


    print(green_box.text.strip())

finally:

    driver.quit()







