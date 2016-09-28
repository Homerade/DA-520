#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NOTE: to use this template, you need to first install pip and install tweepy

import tweepy
import time

# REPLACE these strings with the corresponding information from your Twitter application:
CONSUMER_KEY = '123456789abcdefg'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '123456789abcdefg'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '123456789abcdefg'#keep the quotes, replace this with your access token
ACCESS_SECRET = '123456789abcdefg'#keep the quotes, replace this with your access token secret

# Don't touch this :)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Put your code below this line!
# My code here will tweet "Tweet tweet" every 15 minutes, 100,000 times. (Will finish in ~3 years).

for i in range(0,100000):
	api.update_status("Tweet tweet") # THIS LINE SENDS THE TWEET: "Tweet tweet"
	time.sleep(900) #Tweet every 15 minutes
