import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_browser(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    browser.maximize_window()
    wait = WebDriverWait(browser, 10, )

    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")
    browser.find_element(By.NAME, "zip-code").send_keys("")
    browser.find_element(By.CSS_SELECTOR, ".btn-outline-primary").click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert "alert-danger" in browser.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class"), "Поле не имеет красный цвет"

    elements = ["first-name", "last-name", "address", "e-mail", "phone", "city", "company"]

    for element_class in elements:
        element = browser.find_element(By.ID, element_class)
        assert "alert-success" in element.get_attribute("class"), f"Поле {element_class} не имеет зеленый цвет"






