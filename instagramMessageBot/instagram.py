import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

WAIT_TIME = 10
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

class Instagram:
    def __init__(self):
        self.chrome_driver_path = "C:/Users/Yogesh/OneDrive/Desktop/chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(WAIT_TIME)
        username = self.driver.find_element(By.CSS_SELECTOR, "._ab3b ._aa48 input")
        password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        username.send_keys("YOUR USERNAME")
        password.send_keys("YOUR PASSWORD")
        password.send_keys(Keys.ENTER)
        time.sleep(WAIT_TIME)

    def send_message(self, id):
        self.driver.get(f"https://www.instagram.com/direct/t/{id}")
        time.sleep(WAIT_TIME)
        try:
            not_now_btn = self.driver.find_element(By.CLASS_NAME, "_a9_1")
            not_now_btn.click()
            time.sleep(WAIT_TIME)
        except NoSuchElementException as e:
            print(e)
        msg_box = self.driver.find_element(By.CSS_SELECTOR, '._acrb textarea')
        msg_box.send_keys("This message is sent by a bot. Please ignore.")
        msg_box.send_keys(Keys.ENTER)
        time.sleep(WAIT_TIME)
