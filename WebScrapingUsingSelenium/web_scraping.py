from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def launch_application(browser):
    browser.get("https://www.amazon.in/")
    browser.maximize_window()
    browser.implicitly_wait(10)


def search_product(browser, item_name):
    search_box = browser.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(item_name)
    search_box.submit()
    browser.find_element(By.XPATH, "//span[text()='Apple']/preceding-sibling::div").click()


def data_scraping(browser):
    title = []
    cost = []
    title_elements = browser.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    cost_elements = browser.find_elements(By.XPATH,
                                          "//div[contains(@class, 'a-color-base')]//span[@class='a-price-whole']")
    for t in title_elements:
        # print(t.text)
        title.append(t.text.strip())
    # print("*"*100)
    for c in cost_elements:
        # print(c.text)
        cost.append(c.text.strip())

    zipped_tuple = zip(title, cost)
    with open("WebScrapingUsingSelenium/scrapped_data.csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer_obj = csv.writer(csv_file)
        # writer_obj.writerow("web scraping completed")
        for val in list(zipped_tuple):
            writer_obj.writerow(val)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    launch_application(driver)
    search_product(driver, "Apple iPhone 13")
    data_scraping(driver)
    driver.quit()
