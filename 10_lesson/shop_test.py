import allure
from selenium import webdriver
from ShopPage import ShopPage  # Предполагаем, что класс находится в папке pages


# --- Декораторы Allure для метаданных теста ---
@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Процесс покупки")
@allure.title("Оформление заказа и проверка суммы")
@allure.description(
    "Тест проверяет полный цикл покупки: авторизация, добавление товаров в корзину, "
    "оформление заказа и проверку итоговой суммы."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page():
    """
    Основной сценарий покупки в интернет-магазине.
    """
    driver = webdriver.Firefox()

    try:
        # Инициализируем объект страницы
        shop_page = ShopPage(driver)

        # --- Шаги теста, размеченные через вызовы методов класса ---
        # (Сами методы класса будут размечены декоратором @allure.step)
        shop_page.open()
        shop_page.authorization()
        shop_page.add_to_cart()
        shop_page.in_cart()
        shop_page.click_checkout()
        shop_page.fill_form(
            first_name="Сергей", last_name="Козлов",
            postal_code="157810"
        )

        # --- Проверка (assert), размеченная как отдельный шаг ---
        with allure.step("Проверка итоговой суммы в корзине"):
            shop_page.checking_total_amount()

    finally:
        # Гарантированное закрытие браузера
        driver.quit()