import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from shop_pages import LoginPage, MainShopPage, CartPage, CheckoutPage


@allure.title("Комплексная покупка в SauceDemo")
@allure.description(
    "Тест проверяет добавление 3 товаров и сверку итоговой суммы"
)
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_purchase() -> None:
    """Тест-кейс для проверки полного цикла покупки в магазине."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    login_page = LoginPage(driver)
    main_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавление товаров в корзину"):
            main_page.add_to_cart("sauce-labs-backpack")
            main_page.add_to_cart("sauce-labs-bolt-t-shirt")
            main_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Оформление заказа"):
            main_page.go_to_cart()
            cart_page.checkout()
            checkout_page.fill_form("Елена", "Ахмедова", "660131")

        with allure.step("Проверка итоговой стоимости"):
            total = checkout_page.get_total_price()
            expected_total = "Total: $58.29"
            assert total == expected_total, f"Ошибка! Получено: {total}"

    finally:
        driver.quit()
