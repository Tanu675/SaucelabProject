from Pages.product_page import productsearch
from Pages.login_page import loginpage1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image

def test_add_single_product(driver):
    login_page = loginpage1(driver)
    login_page.enter_validcreds("standard_user","secret_sauce")

    product = productsearch(driver)
    product.add_product_to_cart("Sauce Labs Bike Light")
    product.go_to_cart()
    screen_shotpath= r'C:\Users\MY PC\Desktop\Academy_POM\addtocart.png'
    driver.save_screenshot(screen_shotpath)
    image=Image.open(screen_shotpath)
    image.show()

def test_add_multiple_product(driver):
    login_page = loginpage1(driver)
    login_page.enter_validcreds("standard_user","secret_sauce")

    product = productsearch(driver)
    product.add_product_to_cart("Sauce Labs Bike Light")
    product.add_product_to_cart("Sauce Labs Backpack")
    product.add_product_to_cart("Sauce Labs Fleece Jacket")
    product.add_product_to_cart("Sauce Labs Onesie")

    product.go_to_cart()