# -*- coding: utf-8 -*-

import tweepy
import time
import random
from PyDictionary import PyDictionary
from random import randint

dictionary=PyDictionary()

consumer_key = 'nnxxUoUHW9mntZNZA1qE5Ebt9'
consumer_secret = 'kY8Nz2OEhHqr5pGcaZbSHaqirEvpjOiXdllyvGU5FFAiWIFasj'
access_key = '779492291501318146-91pmk2x9fb9bYur4Zvzp1dVRnRloPOB'
access_secret = 'Ni2JEOFe3hgmU32oxseJKLaAQYQPMZqv5IGAMI2qmfUNo'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#parsing
cycle = ""
synPhrase = ""
quotesTxt = open('synPhrase_quotes.txt', 'r')
lineParse = quotesTxt.read().split("\n")
quotesOnly = lineParse[::3]
# cleanser = quotesOnly[0].lower().replace('.','').replace(',','').replace(';','')
# wordParse = cleanser.split(" ")

for n in range(0, (len(quotesOnly))):
	cleanser = quotesOnly[n].lower().replace('.','').replace(',','').replace(';','')
	wordParse = cleanser.split(" ")

for i in range(0, (len(wordParse))):
	synonyms = dictionary.synonym(wordParse[i])
	try:
		synPhrase = synPhrase + " " + random.choice(synonyms)
	except "{0} has no Synonyms in the API":
		return synPhrase = synPhrase + " " + wordParse[i]
		
	# try: 
	# 	if wordParse[i] == 'the' or wordParse[i] == 'to' or wordParse[i] == 'an' or wordParse[i] == 'your' or wordParse[i] == 'is' or wordParse[i] == 'about' or wordParse[i] == 'not' or wordParse[i] == 'a'  or wordParse[i] == 'it'  or wordParse[i] == 'of'  or wordParse[i] == 'and' or wordParse[i] == 'but' or wordParse[i] == 'into' or wordParse[i] == 'in' or wordParse[i] == 'only' or wordParse[i] == 'at' or wordParse[i] == 'any' or wordParse[i] == 'you' or wordParse[i] == 'are' or wordParse[i] == 'does' or wordParse[i] == "don't" or wordParse[i] == "doesn't" or wordParse[i] == "can't" or wordParse[i] == 'are':
	# 		synPhrase = synPhrase + " " + wordParse[i]
	# 	else:
	# 		synPhrase = synPhrase + " " + random.choice(synonyms)
	# except "{0} has no Synonyms in the API":
	# 	synPhrase = synPhrase + " " + random.choice(synonyms)		
			


	# except "{0} has no Synonyms in the API":
	# 	synPhrase = synPhrase + " " + random.choice(synonyms)


print synPhrase