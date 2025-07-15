from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from faker import Faker
fake = Faker()


def test_registration_valid():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    first_name = driver.find_element(by=By.ID, value="input-firstname")
    first_name.send_keys(fake.first_name())

    last_name = driver.find_element(by=By.ID, value="input-lastname")
    last_name.send_keys(fake.last_name())

    email = driver.find_element(by=By.ID, value="input-email")
    email.send_keys(fake.email())

    telephone = driver.find_element(by=By.ID, value="input-telephone")
    telephone.send_keys(fake.phone_number())

    Password = driver.find_element(by=By.ID, value="input-password")
    Password.send_keys("Html12344")

    Password_confirm = driver.find_element(by=By.ID, value="input-confirm")
    Password_confirm.send_keys("Html12344")

    subscribe = driver.find_element(by=By.NAME, value="newsletter")
    subscribe.click()

    privacy_policy = driver.find_element(by=By.NAME, value="agree")
    subscribe.click()
    time.sleep(5)