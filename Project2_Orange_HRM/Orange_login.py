import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
.sleep(10)
username = driver.find_element(by=By.NAME,value = "username")
username.send_keys("Admin")
password = driver.find_element(by=By.NAME,value = "password")
password.send_keys("admin123")
login = driver.find_element(by=By.CSS_SELECTOR,value = ".oxd-button")
login.click()driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
