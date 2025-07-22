from Pages.product_page import productsearch
from Pages.login_page import loginpage1
from Pages.checkout_page import checkoutpg
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image

def test_checkout11(driver):

    login_page = loginpage1(driver)
    login_page.enter_validcreds("standard_user","secret_sauce")
    product = productsearch(driver)
    product.add_product_to_cart("Sauce Labs Bike Light")
    product.go_to_cart()
    
    checkout1=checkoutpg(driver)
    checkout1.checkout()
    
