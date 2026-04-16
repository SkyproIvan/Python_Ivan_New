from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://uitestingplayground.com/dynamicid/")
sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

sleep(5)
driver.quit()

