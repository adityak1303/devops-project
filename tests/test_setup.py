from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


URL = "http://127.0.0.1:5000"
LOGIN_PAGE = URL + '/login'
SIGNUP_PAGE = URL + '/register'
LOCATE_PAGE = URL + '/locate'
DETAILS_PAGE = URL + '/details'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
#driver.maximize_window()


if __name__ == "__main__":
    print("test_setup file")
