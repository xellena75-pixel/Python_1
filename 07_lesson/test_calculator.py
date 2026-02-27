import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_slow_calculator():
    # Настройка драйвера Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
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
        expected = "15"
        error_message = f"Ожидался результат {expected}, но получен {result}"
        assert result == expected, error_message

    finally:
        # Закрытие браузера
        driver.quit()


