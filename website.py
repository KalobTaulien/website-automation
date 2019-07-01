from selenium import webdriver
import os

# This gets the project path and then gets the chromedriver file to use in the script
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

# Specify the browser to use and the driver to use
browser = webdriver.Chrome(executable_path=DRIVER_BIN)

# Get web addy
browser.get('http://houseboat2018.ca/login/index.php')

# Get page elements
username = browser.find_element_by_id('login_input_username')
password = browser.find_element_by_id('login_input_password')
login_button = browser.find_element_by_css_selector('.form-signin button')

# Do stuff to page elements
# send keys enters information in to the inputs
username.send_keys('steven')
password.send_keys('nevets')
login_button.click()
