from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Caminho opcional do driver se não estiver no PATH
driver = webdriver.Firefox()  # ou webdriver.Firefox()

try:
    # Abre o site
    driver.get("https://www.saucedemo.com/")

    # Aguarda a página carregar
    time.sleep(2)

    # Encontra os campos de login e senha
    username_input = driver.find_element(By.NAME, "user-name")
    password_input = driver.find_element(By.NAME, "password")

    # Preenche os campos
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    password_input.send_keys(Keys.RETURN)  # Pressiona Enter

    time.sleep(3)

    # Verifica se o login foi bem-sucedido
    assert "Products" in driver.page_source
    print("✅ Teste de login passou!")

except Exception as e:
    print(f"❌ Teste falhou: {e}")

finally:
    driver.quit()