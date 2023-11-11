""" stale element reference interaction"""

from selenium import webdriver

def test_take_screenshot():
    """ screenshot """
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.get_screenshot_as_file("./selenium4/screenshot.png")
    driver.close()
