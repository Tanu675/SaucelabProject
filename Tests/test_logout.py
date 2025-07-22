from Pages.product_page import productsearch
from Pages.login_page import loginpage1
from Pages.checkout_page import checkoutpg
from Pages.finish_page import finish
from Pages.logout_page import logout1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image

def test_Logout(driver):
    login_page = loginpage1(driver)
    login_page.enter_validcreds("standard_user","secret_sauce")
    product = productsearch(driver)
    product.add_product_to_cart("Sauce Labs Bike Light")
    product.go_to_cart()
    
    checkout1=checkoutpg(driver)
    checkout1.checkout()

    details=finish(driver)
    details.filldetails('Tanu','Rathore','452001')
    details.finish_checkout()

    loggingout3=logout1(driver)
    loggingout3.logout()