from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC 
from PIL import Image
class productsearch:
    def __init__(self,driver):
         self.driver= driver
         
    def add_product_to_cart(self, product_name):
         inventorysearch = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
         for product in inventorysearch :
              name= product.find_element(By.CLASS_NAME,"inventory_item_name").text
              print(name)
              if product_name ==name:
                   product.find_element(By.CLASS_NAME,"btn_inventory").click()
                   break
    def go_to_cart(self):
         self.driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
             

    


