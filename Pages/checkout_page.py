from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image
class checkoutpg:
     def __init__(self, driver):
         self.driver = driver
         self.checkoutbutton =(By.XPATH ,'//*[@id="cart_contents_container"]/div/div[2]/a[2]')
         
     def checkout(self):
        self.driver.find_element(*self.checkoutbutton).click()
     