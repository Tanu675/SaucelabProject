from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image

class finish:
    def __init__(self,driver):
        self.driver=driver
        self.firstname = (By.CLASS_NAME,"first-name")
        self.lastname=(By.ID,"last-name")
        self.zipcode=(By.ID,"postal-code")
        self.continuebutton=(By.XPATH,'//*[@id="checkout_info_container"]/div/form/div[2]/input')
        self.finishbuttoun=(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]')
    
    

    def filldetails(self,name,lastname,zipcode):
        self.driver.find_element(*self.firstname).send_keys(name)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.continuebutton).click()

    def finish_checkout(self):
        self.driver.find_element(*self.finishbuttoun).click()
        