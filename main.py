import internet_speed_tester
import twitter_bot
from pprint import pprint
import os

#Promised Upload and Download speed from your ISP
PROMISED_DOWN = 150
PROMISED_UP = 10

#Import the twitter username and password environemnt variables
TWITTER_USER = os.environ['TWITTER_USER']
TWITTER_PASS = os.environ['TWITTER_PASS']

#Pull the current download and upload speed. Note the difference b/w bandwidth and your individual download speed
speed_test = internet_speed_tester.speed_tester()
speed_dict = speed_test.get_internet_speed()

#Check if we need to send out a tweet
if float(speed_dict['download_speed']) < PROMISED_DOWN or float(speed_dict['upload_speed']) < PROMISED_UP:
    #Initialize the twitter bot
    twit_bot = twitter_bot.Twitter_Bot(TWITTER_USER, TWITTER_PASS)
    #Send out the tweet
    twit_bot.tweet_storm(speed_dict=speed_dict, promised_up=PROMISED_UP, promised_down=PROMISED_DOWN)