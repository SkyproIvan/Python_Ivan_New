from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ShopPage:
    """
    Класс-описание страниц интернет-магазина SauceDemo.
    Инкапсулирует локаторы и методы для взаимодействия с элементами.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация объекта страницы.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу магазина")
    def open(self) -> None:
        """
        Переход на главную страницу магазина.

        Returns:
            None
        """
        self.driver.get(self.url)

    @allure.step("Авторизация под пользователем")
    def authorization(self) -> None:
        """
        Выполнение входа в систему под стандартным пользователем.

        Returns:
            None
        """
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Добавить товары в корзину")
    def add_to_cart(self) -> None:
        """
        Добавляет предопределенный список товаров в корзину.

        Returns:
            None
        """
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        for item in items:
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")
                )
            ).click()

    @allure.step("Перейти в корзину")
    def in_cart(self) -> None:
        """
        Переход на страницу просмотра корзины.

        Returns:
            None
         """
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def click_checkout(self):
        pass

    def fill_form(self, first_name, last_name, postal_code):
        pass

    def checking_total_amount(self):
        pass


@allure.step("Нажать кнопку 'Checkout'")
def click_checkout(self) -> None:
    """
    Нажатие на кнопку 'Checkout' на странице корзины.

    Returns:
        None
     """
    self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


@allure.step("Заполнить форму с информацией о покупателе")
def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
    """
    Заполнение формы с данными покупателя на этапе оформления заказа.

    Args:
        first_name (str): Имя покупателя.
        last_name (str): Фамилия покупателя.
        postal_code (str): Почтовый индекс.

    Returns:
        None
     """
    self.driver.find_element(By.ID, "first-name").send_keys(first_name)
    self.driver.find_element(By.ID, "last-name").send_keys(last_name)
    self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    self.driver.find_element(By.ID, "continue").click()


@allure.step("Проверить итоговую сумму заказа")
def checking_total_amount(self) -> None:
    """
    Проверяет, что итоговая сумма заказа соответствует ожидаемому значению.

    Returns:
        None

    Raises:
        AssertionError: Если итоговая сумма не равна "Total: $58.29".
    """
    total = (
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        .text
    )
    assert total == "Total: $58.29", (
        f"Итоговая сумма не равна $58.29. Фактическая сумма: {total}"
    )