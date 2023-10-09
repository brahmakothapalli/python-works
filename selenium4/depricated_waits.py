"""broken links with filter method"""
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_broken_links(link):
    # logging.info("Total links count %s", len(links))
    url = link.get_attribute("href")
    code = requests.get(url, timeout=10).status_code
    return True if code == 200 else False


def test_broken_links():
    """test"""
    logging.info("testing broken links :: test_broken_links")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    links = driver.find_elements(By.TAG_NAME, "a")
    names = list(filter(get_broken_links, links))
    print(names)
