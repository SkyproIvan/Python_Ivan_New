from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import pytest

class CalculatorPage:
    """
    Класс-описание страницы 'Slow Calculator'.
    Создает локаторы и методы для взаимодействия с элементами.
    """


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 17)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Переходит на страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Установить задержку выполнения операций на {delay_value} мс")
    def set_delay(self, delay_value: int) -> None:
        """Устанавливает значение задержки в секундах."""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    @allure.step("Нажать на кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """Нажимает на кнопку с указанным текстом."""
        xpath = f"//span[contains(normalize-space(), '{button_text}')]"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Выполнить вычисление по выражению: {expression}")
    def perform_calculation(self, expression: list[str]) -> None:
        """Выполняет последовательность нажатий кнопок."""
        for button in expression:
            self.click_button(button)

    @allure.step("Получить текущий результат с экрана")
    def get_result(self) -> str:
        """Возвращает текст, отображаемый на экране калькулятора."""
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    @allure.step("Проверить, что результат равен '{expected_result}'")
    def verify_result(self, expected_result: str, timeout: int = 17) -> None:
        """Ожидает появления ожидаемого результата на экране."""
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
        )