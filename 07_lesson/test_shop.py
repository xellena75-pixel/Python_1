import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from shop_pages import LoginPage, MainShopPage, CartPage, CheckoutPage


def test_saucedemo_purchase():
    # Настройка Firefox с указанием пути к браузеру
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    # Инициализация объектов страниц
    login_page = LoginPage(driver)
    main_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        # 1. Авторизация
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Добавление товаров
        main_page.add_to_cart("sauce-labs-backpack")
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("sauce-labs-onesie")

        # 3. Переход в корзину и Checkout
        main_page.go_to_cart()
        cart_page.checkout()

        # 4. Заполнение формы
        checkout_page.fill_form("Елена", "Ахмедова", "660131")

        # 5. Проверка итоговой суммы
        total = checkout_page.get_total_price()
        assert total == "Total: $58.29", f"Ожидалось $58.29, но получили {total}"

    finally:
        # Закрытие браузера
        driver.quit()

