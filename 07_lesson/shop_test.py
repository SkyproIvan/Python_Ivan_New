from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from internet_shop_page import ShopPage


def test_shop_page():
    driver = webdriver.Firefox()
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.authorization()
    shop_page.add_to_cart()
    shop_page.in_cart()
    shop_page.click_checkout()
    shop_page.fill_form(
            first_name="Сергей", last_name="Козлов",
            postal_code="157810")
    shop_page.checking_total_amount()
    driver.quit()