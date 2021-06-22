from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
import time


class speed_tester:
    def __init__(self):
        # Set up the webdriver
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        # Go to the speedtest website
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        # Find and click the button to start the test
        check_speed_button = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        check_speed_button.click()
        time.sleep(40)
        # Find the upload and download speed and return it as a dictionary
        download = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        speed_dict = {
            'download_speed': download.text,
            'upload_speed': upload.text
        }
        # Exit out of the browser
        self.driver.quit()
        #Return the download speed and upload speed dictionary
        return speed_dict
