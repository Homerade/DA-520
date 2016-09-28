# -*- coding: utf-8 -*-

import tweepy

import time

import random

from PyDictionary import PyDictionary

from random import randint

dictionary=PyDictionary()

consumer_key = 'nnxxUoUHW9mntZNZA1qE5Ebt9'
consumer_secret = 'kY8Nz2OEhHqr5pGcaZbSHaqirEvpjOiXdllyvGU5FFAiWIFasj',
access_key = '779492291501318146-91pmk2x9fb9bYur4Zvzp1dVRnRloPOB',
access_secret = 'Ni2JEOFe3hgmU32oxseJKLaAQYQPMZqv5IGAMI2qmfUNo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


#parsing

synPhrase = ""

quotesTxt = open('synPhrase_quotes.txt', 'r')

lineParse = quotesTxt.read().split("\n")

quotesOnly = lineParse[::3]

# for i in range(0, (len(lineParse))):

#  	indexParse = lineParse[i].split(",")

#  	synPhrase = synPhrase + indexParse

print quotesOnly



#made a list out of each quote
# for i in range(0, (len(quotesOnly))):

# 	wordParse = quotesOnly[i].split(" ")

# 	#synPhrase = synPhrase + wordParse  #--not working error: cannot concatenate str and list objects

# 	print wordParse


	# wordParse = lineParse[0].split(" ")