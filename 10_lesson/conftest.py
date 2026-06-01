import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для управления веб-драйвером Chrome.
    Автоматически устанавливает и обновляет chromedriver.
    """
    # Настройка (Setup)
    print("\nЗапуск драйвера...")  # Сообщение для наглядности
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)  # Можно оставить небольшой implicit wait для поиска элементов
    driver.maximize_window()

    # Передаем управление тесту
    yield driver

    # Очистка (Teardown) - выполнится после теста
    print("\nЗакрытие драйвера...")
    driver.quit()