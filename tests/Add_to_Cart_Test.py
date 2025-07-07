# from selenium import webdriver # type: ignore
# from selenium.webdriver.common.by import By # type: ignore

# BASE_URL = "https://www.saucedemo.com/"

# def open_browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(BASE_URL)
#     return driver

# def login(driver, username="standard_user", password="secret_sauce"):
#     driver.get(BASE_URL)
#     driver.find_element(By.ID, "user-name").send_keys(username)
#     driver.find_element(By.ID, "password").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR,  "input#login-button").click()
#     time.sleep(1)

# def test_add_item_to_cart():
#     driver = open_browser()
#     login(driver)

#     driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
#     time.sleep(1)

#     cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
#     assert cart_badge == "1", "Cart count is not 1"
#     print("✅ Single item added to cart successfully!")

#     driver.quit()

# def test_add_items_to_cart():
#     driver = open_browser()
#     login(driver)

#     buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
#     for i in range (2):
#         buttons[i].click()
#         time.sleep(1)

#     cart_badge = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
#     assert cart_badge == "2", "Cart count is not 2"
#     print("✅ Multiple items added to cart successfully!")

#     driver.quit()

# def test_remove_item_from_cart():
#     driver = open_browser()
#     login(driver)

#     driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
#     time.sleep(1)

#     driver.find_element(By.XPATH, "//button[text()='Remove']").click()
#     time.sleep(1)

#     badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#     assert len(badges) == 0, "Cart badge should be gone"
#     print("✅ Item removed from cart!")

#     driver.quit()

# def test_view_cart():
#     driver = open_browser()
#     login(driver)

#     item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").click()

#     driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
#     time.sleep(1)

#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     time.sleep(1)

#     cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
#     assert item_name == cart_item_name, "Item in cart doesn't match!"
#     print("✅ Item in cart matches the one you added!")

#     driver.quit()

# def run_all_tests():
#     for test in [
#         test_add_item_to_cart,
#         test_add_items_to_cart,
#         test_remove_item_from_cart,
#         test_view_cart
#     ]:
#         try:
#             test()
#             print(f"{test.__name__}: ✅ Passed")
#         except AssertionError:
#             print(f"{test.__name__}: ❌ Failed (AssertionError)")
#         except Exception as e:
#             print(f"{test.__name__}: ❌ Failed ({e})")
#         time.sleep(2)

# if __name__ == "__main__":
#     run_all_tests()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

def test_add_item_to_cart():
    driver = open_browser()
    login(driver)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1", "Cart count is not 1"
    print("✅ Single item added to cart successfully!")

    driver.quit()

def test_add_items_to_cart():
    driver = open_browser()
    login(driver)

    # Wait for all "Add to cart" buttons to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']"))
    )

    # Get all buttons and click the first two
    add_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
    add_buttons[0].click()
    time.sleep(1)
    add_buttons[1].click()
    time.sleep(1)

    # Verify the cart badge shows 2
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "2", "Cart count is not 2"
    print("✅ Multiple items added to cart successfully!")

    driver.quit()

def test_remove_item_from_cart():
    driver = open_browser()
    login(driver)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Add to cart'])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']"))).click()

    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    print("✅ Item removed from cart!")

    driver.quit()

def test_view_cart():
    driver = open_browser()
    login(driver)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    cart_item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert item_name == cart_item_name, "Item in cart doesn't match!"
    print("✅ Item in cart matches the one you added!")

    driver.quit()

def run_all_tests():
    for test in [
        test_add_item_to_cart,
        test_add_items_to_cart,
        test_remove_item_from_cart,
        test_view_cart
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
