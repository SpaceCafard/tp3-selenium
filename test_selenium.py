from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_selenium():
    driver = webdriver.Firefox(executable_path='C:\Users\SpaceCafard\Downloads\selenium_project/geckodriver.exe') 
    driver.get("http://127.0.0.1:5000/") 
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    username_field.send_keys('user')
    password_field.send_keys('password')
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Welcome to your dashboard!" in driver.page_source
    driver.quit()