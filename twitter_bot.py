from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
import time


class Twitter_Bot:
    def __init__(self, user_name, password):
        #Set up the webdriver and initialize the username and password variables
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.user = user_name
        self.password = password

    def tweet_storm(self, speed_dict, promised_up, promised_down):
        #Go to the twitter website
        self.driver.get("https://twitter.com/login")
        time.sleep(10)
        #Find the username, password field and sign in button
        user_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        pass_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        #Enter the username, password and click the sign in button
        user_field.send_keys(self.user)
        pass_field.send_keys(self.password)
        button.click()
        time.sleep(10)

        #Generate the isp tweet, Replace @Bell_Support with your isp
        isp_tweet = 'Hey @Bell_Support, why is my internet speed ' + speed_dict['download_speed'] + ' down/ ' + \
                    speed_dict['upload_speed'] + ' up when I pay for ' + str(promised_down) + ' down/ ' + str(promised_up) +' up?'
        #Find the tweet field and the submit button
        tweet_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        #Enter the isp tweet
        tweet_field.send_keys(isp_tweet)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        #Send out the tweet
        tweet_button.click()
        self.driver.quit()
        return