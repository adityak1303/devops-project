from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


URL = "http://127.0.0.1:5000"
LOGIN_PAGE = URL + '/login'
SIGNUP_PAGE = URL + '/register'
LOCATE_PAGE = URL + '/locate'
DETAILS_PAGE = URL + '/details'


driver = webdriver.Chrome()
driver.maximize_window()


if __name__ == "__main__":
    print("test_setup file")
