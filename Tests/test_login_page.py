from Pages.login_page import loginpage1
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image

def test_validating_login_step(driver):
    login_page = loginpage1(driver)
    login_page.enter_validcreds("standard_user","secret_sauce")
    driver.implicitly_wait(5)
    screenshot_path=r'C:\Users\MY PC\Desktop\Academy_POM\screenshot\login.png'
    driver.save_screenshot(screenshot_path)
    image = Image.open(screenshot_path)
    image.show()


    
    # WebDriverWait(driver, 10).until(EC.title_contains("Swag Labs")) 
    assert "Swag Labs" in driver.title
