import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com"

    @allure.step("Открыть страницу входа")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class MainShopPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        formatted_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{formatted_name}")
        self.driver.find_element(*locator).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Нажать Checkout")
    def checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step(
        "Заполнить данные: {first_name} {last_name}, ZIP: {zip_code}"
    )
    def fill_form(self,
                  first_name: str,
                  last_name: str,
                  zip_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить общую сумму заказа")
    def get_total_price(self) -> str:
        locator = (By.CLASS_NAME, "summary_total_label")
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
