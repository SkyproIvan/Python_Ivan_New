import pytest
import allure
from CalculatorPage import CalculatorPage


# --- Декораторы для метаданных теста ---
@allure.feature("Калькулятор")  # Группа тестов (например, "Авторизация", "Корзина")
@allure.story("Арифметические операции")  # Конкретный сценарий в рамках фичи
@allure.title("Проверка операции сложения 7 + 8")  # Читаемое название теста в отчете
@allure.description("Тест проверяет, что калькулятор корректно выполняет сложение двух чисел.")  # Подробное описание
@allure.severity(allure.severity_level.NORMAL)  # Важность теста (BLOCKER, CRITICAL, NORMAL, MINOR)
# Сам тест использует фикстуру 'driver' из conftest.py
def test_calculator_addition(driver):
    # Инициализируем объект страницы с драйвером из фикстуры
    calc_page = CalculatorPage(driver)

    # Вызовы методов, которые уже размечены декоратором @allure.step
    calc_page.open()
    calc_page.set_delay(18)
    calc_page.perform_calculation(['7', '+', '8', '='])

    # Получаем результат для финальной проверки
    actual_result = calc_page.get_result()

    # Разметка проверки (assert) с помощью контекстного менеджера
    with allure.step("Финальная проверка результата"):
        assert actual_result == "15", f"Ожидалось '15', но получено '{actual_result}'"