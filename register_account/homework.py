import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
first_name = driver.find_element(by=By.ID,value = "input-firstname")
first_name.send_keys("Tanzida")
last_name = driver.find_element(by=By.ID,value = "input-lastname")
last_name.send_keys("Khan")
email = driver.find_element(by=By.ID,value = "input-email")
email.send_keys("tanzida@12344.com")
telephone = driver.find_element(by=By.ID,value = "input-telephone")
telephone.send_keys("01234567")
Password = driver.find_element(by=By.ID,value = "input-password")
Password.send_keys("Html12344")
Password_confirm = driver.find_element(by=By.ID,value = "input-confirm")
Password_confirm.send_keys("Html12344")
subscribe = driver.find_element(by=By.NAME,value = "newsletter")
subscribe.click()
privacy_policy = driver.find_element(by=By.NAME,value = "agree")
subscribe.click()
time.sleep(5)






