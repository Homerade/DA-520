# -*- coding: utf-8 -*-

import tweepy

import time

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

synFrost = ""

frost = ['Two', 'roads', 'diverged', 'in*', 'a*', 'wood', ',*', 'and*', 'I*', ',*', 'I*', 'took', 'the*', 'one*', 'less', 'traveled', 'by*', 'and*', 'that*', 'has*', 'made', 'all*', 'the*', 'difference']


for i in range (0, (len(frost))):
	
	synonym = dictionary.synonym(frost[i])
	
	if frost[i][-1] == '*':
	
		synFrost = synFrost + " " + frost[i][:len(frost[i])-1]
	
	elif len(synonym) is True:
	
		synFrost = synFrost + " " + frost[i]
	
	else: synFrost = synFrost + " " + synonym[randint(0, (len(synonym)-1))]	 


print synFrost

#api.update_status("")
#time.sleep(900)