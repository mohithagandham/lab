from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

time.sleep(1)

driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "password").send_keys("test123")
driver.find_element(By.ID, "registerForm").submit()

time.sleep(2)

if "registration successful" in driver.page_source.lower():
    print("✅ Test passed")
else:
    print("❌ Test failed")

driver.quit()
