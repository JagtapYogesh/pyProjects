import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Response:
    def __init__(self):
        self.URL = "https://docs.google.com/forms/d/e/1FAIpQLSf6KfpY6G3IasfynY_aodPsvnQ7mXHlfPCso0Bclcy3J4MQHw/viewform"
        self.chrome_driver_path = 'C:/Users/Yogesh/OneDrive/Desktop/selenium driver/chromedriver.exe'

    def enter_responses(self, property_listings):
        driver = webdriver.Chrome(self.chrome_driver_path)
        for item in property_listings:
            driver.get(self.URL)
            time.sleep(2)
            entry_fields = driver.find_elements(By.CLASS_NAME, "zHQkBf")
            entry_fields[0].send_keys(item["name"])
            entry_fields[1].send_keys(item["location"])
            entry_fields[2].send_keys(item["link"])

            submit_btn = driver.find_element(By.CLASS_NAME, "NPEfkd")
            submit_btn.click()
