from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)  # Wait to see result
    if "Logged In Successfully" in driver.page_source:
        print("✅ Login Successful")
    elif "Your username is invalid!" in driver.page_source or "Your password is invalid!" in driver.page_source:
        print("❌ Login Failed")
    else:
        print("⚠️ Unexpected Result")

    driver.quit()


# Test both cases
test_login("student", "Password123")       # Valid
test_login("wronguser", "wrongpass")       # Invalid
