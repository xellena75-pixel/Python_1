import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет сложение 7 + 8 с задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator() -> None:
    """Тест проверяет сложение чисел с задержкой выполнения операции."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    calc = CalculatorPage(driver)

    try:
        calc.open()
        calc.set_delay(45)

        with allure.step("Выполнить операцию 7 + 8"):
            calc.click_button("7")
            calc.click_button("+")
            calc.click_button("8")
            calc.click_equal()

        with allure.step("Проверить, что результат равен 15"):
            result = calc.get_result()
            assert result == "15", f"Ожидалось 15, но получено {result}"
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
