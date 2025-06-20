from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_selenium():
    driver = webdriver.Chrome()  # Assurez-vous d'avoir ChromeDriver installé
    driver.get("http://127.0.0.1:5000/")

    # Trouver les champs de formulaire et les remplir
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')

    username_field.send_keys('user')
    password_field.send_keys('password')
    password_field.send_keys(Keys.RETURN)

    # Attendre que la page de tableau de bord se charge
    time.sleep(2)

    assert "Welcome to your dashboard!" in driver.page_source
    driver.quit()
