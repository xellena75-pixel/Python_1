from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    driver.get("http://uitestingplayground.com/textinput")


    wait = WebDriverWait(driver, 15)
    input_field = wait.until(EC.element_to_be_clickable((By.ID, "newButtonName")))
    input_field.send_keys("SkyPro")


    blue_button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
    blue_button.click()


    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

    print(blue_button.text)

finally:
    driver.quit()





