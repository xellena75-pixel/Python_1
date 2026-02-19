import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_slow_calculator():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    calc = CalculatorPage(driver)

    try:
        # Шаги по заданию
        calc.open()
        calc.set_delay(45)

        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_equal()

        # Проверка результата
        result = calc.get_result()
        assert result == "15", f"Ожидался результат 15, но получен {result}"

    finally:
        # закрытие браузера
        driver.quit()

