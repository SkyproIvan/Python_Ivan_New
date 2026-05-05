from operator import index

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(browser):
    browser.get("https://www.saucedemo.com")
    wait = WebDriverWait(browser, 50)

    user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
    user_name.send_keys("standard_user")
    user_password = browser.find_element(By.CSS_SELECTOR, "#password")
    user_password.send_keys("secret_sauce")
    login_button = browser.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()
    backpack = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    backpack.click()
    t_shirt = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt.click()
    onesie = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    onesie.click()
    badge = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    badge.click()
    checkout = browser.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()
    first_name = browser.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Иван")
    last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Козлов")
    last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Козлов")
    index_code = browser.find_element(By.CSS_SELECTOR, "#postal-code")
    index_code.send_keys("157800")
    continue_button = browser.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()
    browser.close()
    total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total_element.text
    total_value = total_text.replace("Total: $", "")

    expected_total = "58.29"
    assert total_value == expected_total, f"Ожидалась сумма ${expected_total}, но получили ${total_value}"


    browser.close()








