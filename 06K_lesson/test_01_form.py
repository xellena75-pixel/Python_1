import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver_path = r"C:\Users\Елена\Downloads\edgedriver_win64\msedgedriver.exe"
    service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    try:

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 20)


        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for name, value in fields.items():
            driver.find_element(By.NAME, name).send_keys(value)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert")))

        zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert "alert-danger" in zip_class
        success_ids = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]

        for field_id in success_ids:
            field_class = driver.find_element(By.ID, field_id).get_attribute("class")
            assert "alert-success" in field_class

    finally:
        driver.quit()
































