''' highlight the web element'''
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_highlight_web_element():
    ''' this test highlights web element to be interacted'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    user_name.send_keys("standard_user")
    password.send_keys("secret_sauce")
    driver.execute_script("arguments[0].style.border='3px solid red'", password)
    driver.get_screenshot_as_file("./selenium4/after.png")
    login_button.click()
    

    
    driver.close()
