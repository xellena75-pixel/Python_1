import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    path = r"C:\Users\Елена\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver

    driver.quit()


def test_slow_calculator(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")


    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()

    equal_btn = driver.find_element(By.XPATH, "//span[text()='=']")
    driver.execute_script("arguments[0].click();", equal_btn)

    wait = WebDriverWait(driver, 45)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))


    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15"













