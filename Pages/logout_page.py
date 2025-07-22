from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image
class logout1:
    def __init__(self,driver):
        self.driver = driver
        self.sidebar=(By.XPATH,'//*[@id="menu_button_container"]/div/div[3]/div/button')
        self.logingout = (By.XPATH,'//*[@id="logout_sidebar_link"]')
    def logout(self):
        self.driver.find_element(*self.sidebar).clicl()
        self.driver.find_element(*self.logingout).click()