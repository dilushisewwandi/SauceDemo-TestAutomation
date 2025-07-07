import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

BASE_URL = "https://www.saucedemo.com/"

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    return driver

def test_successful_login():
    driver = open_browser()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
    time.sleep(2)

    assert "inventory.html" in driver.current_url, "❌ Login failed!"
    print("✅ Login test passed!")

    driver.quit()

def test_incorrect_username():
    driver = open_browser()

    driver.find_element(By.ID, "user-name").send_keys("incorrect")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    time.sleep(2)

    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    assert "Username and password do not match" in error_msg, "❌ Error message not displayed correctly." # type: ignore
    print("✅ Incorrect username test passed!")

    driver.quit()

def test_incorrect_password():
    driver = open_browser()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("incorrect")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    time.sleep(2)

    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    assert "Username and password do not match" in error_msg, "❌ Error message not displayed correctly." # type: ignore
    print("✅ Incorrect password test passed!")

    driver.quit()

def test_blank_fields():
    driver = open_browser()

    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
    time.sleep(2)

    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    assert "Username is required" in error_msg, "❌ Error message not displayed correctly." # type: ignore
    print("✅ Blank fields test passed!")

    driver.quit()

def test_lockedout_user():
    driver = open_browser()

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
    time.sleep(2)

    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

    assert "Sorry, this user has been locked out." in error_msg, "❌ Error message not displayed correctly." # type: ignore
    print("✅ Locked-out user login test passed!")

    driver.quit()

def run_all_tests():
    for test in [
        test_successful_login,
        test_incorrect_username,
        test_incorrect_password,
        test_blank_fields,
        test_lockedout_user
    ]:
        try:
            test()
            print(f"{test.__name__}: ✅ Passed")
        except AssertionError:
            print(f"{test.__name__}: ❌ Failed (AssertionError)")
        except Exception as e:
            print(f"{test.__name__}: ❌ Failed ({e})")
        time.sleep(2)


if __name__ == "__main__":
    run_all_tests()

