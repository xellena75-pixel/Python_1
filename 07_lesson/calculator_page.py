from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.wait = WebDriverWait(self.driver, 10)

    # Локаторы
    _DELAY_INPUT = (By.ID, "delay")
    _RESULT_SCREEN = (By.CLASS_NAME, "screen")
    _SPINNER = (By.ID, "spinner")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        # Ожидаем поле, очищаем и вводим задержку
        delay_field = self.wait.until(EC.element_to_be_clickable(self._DELAY_INPUT))
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        # Поиск кнопки по тексту
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        element = self.wait.until(EC.presence_of_element_located(locator))
        # JS-клик обходит ошибку ElementClickIntercepted
        self.driver.execute_script("arguments[0].click();", element)

    def click_equal(self):
        self.click_button("=")

    def get_result(self):
        # Ожидание
        long_wait = WebDriverWait(self.driver, 45)

        # Ждем, пока исчезнет спиннер
        long_wait.until(EC.invisibility_of_element_located(self._SPINNER))

        # Ждем появления числа "15" в поле результата
        long_wait.until(EC.text_to_be_present_in_element(self._RESULT_SCREEN, "15"))

        return self.driver.find_element(*self._RESULT_SCREEN).text




