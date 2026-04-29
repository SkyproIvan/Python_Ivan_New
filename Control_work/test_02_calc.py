import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   yield driver
   driver.quit()

def test_2(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.maximize_window()
    wait = WebDriverWait(browser, 60)

    element = browser.find_element(By.CSS_SELECTOR, "#delay")
    element.clear()
    element.send_keys("45")


    button_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'btn btn-outline-primary' and text() = '7']")))
    button_7.click()
    button_plus = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'operator btn btn-outline-success' and text() = '+']")))
    button_plus.click()
    button_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'btn btn-outline-primary' and text() = '8']")))
    button_8.click()
    button_res = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'btn btn-outline-warning' and text() = '=']")))
    button_res.click()

    try:

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result_screen = browser.find_element(By.CSS_SELECTOR, ".screen")
        total = result_screen.get_attribute("textContent").strip()
        assert total == "15", (
            f"\nПоле не равно 15:\n"
            f"Ожидаемый результат 15")

    except TimeoutException:
        print("Время истекло")
    finally:
        browser.quit()







    




