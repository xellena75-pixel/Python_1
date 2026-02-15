import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    path = r"C:\Users\Елена\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Firefox(service=service)

    # Неявное ожидание для стабильности
    driver.implicitly_wait(10)

    driver.maximize_window()
    yield driver

    driver.quit()


def test_sauce_demo_shop(driver):

    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()


    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    driver.find_element(By.ID, "checkout").click()


    driver.find_element(By.ID, "first-name").send_keys("Елена")
    driver.find_element(By.ID, "last-name").send_keys("Ахмедова")
    driver.find_element(By.ID, "postal-code").send_keys("660131")

    driver.find_element(By.ID, "continue").click()

    wait = WebDriverWait(driver, 10)
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_price_text = total_element.text

    assert total_price_text == "Total: $58.29"


