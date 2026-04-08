from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_login_invalido(driver):
    driver.find_element(By.ID, "username").send_keys("usuario_errado")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    erro = driver.find_element(By.ID, "flash")
    assert "Your username is invalid" in erro.text

def test_login_valido(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    mensagem = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area" in mensagem.text