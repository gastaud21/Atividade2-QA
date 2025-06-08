from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

try:
    # Acessa o site e faz login
    driver.get("https://www.saucedemo.com")
    time.sleep(2)

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce" + Keys.RETURN)
    time.sleep(2)

    # Adiciona um item ao carrinho
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    # Vai para o carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # Clica em "Checkout"
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)

    # Preenche informações de checkout
    driver.find_element(By.ID, "first-name").send_keys("João")
    driver.find_element(By.ID, "last-name").send_keys("Silva")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # Finaliza a compra
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Verifica mensagem de sucesso
    assert "Thank you for your order!" in driver.page_source
    print("✅ Teste de sistema passou com sucesso!")

except Exception as e:
    print(f"❌ Teste falhou: {e}")

finally:
    driver.quit()
