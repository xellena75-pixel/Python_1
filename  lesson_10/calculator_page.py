import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev"
            "slow-calculator.html"
        )
        self.wait = WebDriverWait(self.driver, 10)

    # Локаторы
    _DELAY_INPUT = (By.ID, "delay")
    _RESULT_SCREEN = (By.CLASS_NAME, "screen")
    _SPINNER = (By.ID, "spinner")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self._DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать на кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        xpath = f"//span[text()='{button_text}']"
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Нажать '='")
    def click_equal(self) -> None:
        self.click_button("=")

    @allure.step("Получить итоговый результат")
    def get_result(self) -> str:
        long_wait = WebDriverWait(self.driver, 60)
        long_wait.until(EC.invisibility_of_element_located(self._SPINNER))
        long_wait.until(
            EC.text_to_be_present_in_element(self._RESULT_SCREEN, "15")
        )
        return self.driver.find_element(*self._RESULT_SCREEN).text
