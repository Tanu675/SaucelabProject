import pytest
from selenium import webdriver
from PIL import Image
import time
@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    driver.get("https://www.saucedemo.com/v1/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
