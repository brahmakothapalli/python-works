import imp
import pstats
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

def launch_application():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://web.whatsapp.com")
    return driver


def serach_contact(browser, contact_name):
    try:
        search_contact_box = browser.find_element(By.XPATH, "//div[@title='Search input textbox']")
        search_contact_box.click()
        search_contact_box.send_keys(contact_name)
        time.sleep(5)
        user_contact = browser.find_element(By.XPATH, "//div[@class='_3OvU8']//span[@title='{}']".format(contact_name))
        user_contact.click()
    except Exception as e:
        print(f"Given user {contact_name} is not in contacts")


def send_message(browser, message):
    try:
        type_message_box = browser.find_element(By.XPATH, "//div[@title='Type a message']")
        type_message_box.send_keys(message)
        time.sleep(3)
        send_button = browser.find_element(By.XPATH, "//button[@data-testid='compose-btn-send']")
        send_button.click()
        print('message sent successfully')
    except Exception as e:
        print(f"Failed to send the {message}")
    

if __name__ == '__main__':

    print('launching the browser')
    browser = launch_application()
    print('waiting for the whatsapp web connection')
    time.sleep(15)
    print('searching for the contact')
    contacts_list = ['Amma', 'Harika']
    for name in contacts_list:
        serach_contact(browser, name)
        send_message(browser, "This is Python Bot!")
    browser.quit()