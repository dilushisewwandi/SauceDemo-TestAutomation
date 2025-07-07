import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

BASE_URL = "https://www.saucedemo.com/"

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,  "input#login-button").click()
    time.sleep(2)

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    return driver

def test_view_all_products():
    driver = open_browser()
    login(driver)

    assert "inventory.html" in driver.current_url, "❌ Not redirected to product items!"
    
    print("✅ All product items visible successfully")
    driver.quit()

def get_product_names(driver):
    return [item.text for item in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

def get_product_prices(driver):
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    return [float(p.text.replace("$", "")) for p in price_elements]

def test_sort_name_atoz():
    driver = open_browser()
    login(driver)

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("az")
    time.sleep(2)

    names = get_product_names(driver)
    assert names == sorted(names), "❌ Product names are not sorted A to Z"

    print("✅ Products sorted by Name (A to Z)")
    driver.quit()

def test_sort_price_lowtohigh():
    driver = open_browser()
    login(driver)

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")
    time.sleep(2)

    prices = get_product_prices(driver)
    assert prices == sorted(prices), "❌ Prices not sorted from low to high"

    print("✅ Products sorted by Prices (low to high)")
    driver.quit()

def test_product_names_and_prices():
    driver = open_browser()
    login(driver)

    expected_products = {
    "Sauce Labs Backpack": 29.99,
    "Sauce Labs Bike Light": 9.99,
    "Sauce Labs Bolt T-Shirt": 15.99,
    "Sauce Labs Fleece Jacket": 49.99,
    "Sauce Labs Onesie": 7.99,
    "Test.allTheThings() T-Shirt (Red)": 15.99
    }
    
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for item in items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        price_text = item.find_element(By.CLASS_NAME, "inventory_item_price").text
        price = float(price_text.replace("$", ""))

        assert name in expected_products, f"❌ Unexpected product name: {name}" # type: ignore
        assert price == expected_products[name], f"❌ Price mismatch for {name}: {price} != {expected_products[name]}" # type: ignore

    print("✅ Product names and prices are correct")
    driver.quit()

def run_all_tests():
    for test in [
        test_view_all_products,
        test_sort_name_atoz,
        test_sort_price_lowtohigh,
        test_product_names_and_prices
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
