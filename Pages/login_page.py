import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
import time

class loginpage1:
    def __init__(self,driver):
        self.driver=driver

        self.wait = WebDriverWait(driver,10)
        self.username = (By.XPATH , "//input[@type='text' and @class='form_input']")
        self.password=(By.ID,"password")
        self.login=(By.ID,"login-button")
        self.logger = self.setup_logger()
        
        # self.product =(By.XPATH,"//*[@id='item_4_title_link']/div")
    def enter_validcreds(self,username,password):
        # self.wait.until(EC.visibility_of_element_located(*self.username)).send_keys(username)
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        
        self.driver.implicitly_wait(2)
        self.driver.find_element(*self.login).click()
    
        

