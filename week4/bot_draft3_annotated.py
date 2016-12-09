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


#singling out, stripping and splitting text

#selector = random.choice(quotesOnly) ---chose random quote (but repeats became a problem)

for x in range(0, (len(quotesOnly))):

	cleanser = quotesOnly[x].lower().replace('.','').replace(',','').replace(';','')

	wordParse = cleanser.split(" ")

	#cycle = cycle + str(wordParse)  .....my attempt at cycling through the loop (made a series of lists: one for each quote parsed by word)

	#finding synonyms
	# for i in range(0, (len(wordParse))):

	# 		synonyms = dictionary.synonym(wordParse[i])

	# 		#randSyn = random.choice(synonyms)

	# 		if wordParse[i] == 'the' or wordParse[i] == 'to' or wordParse[i] == 'an' or wordParse[i] == 'your' or wordParse[i] == 'is' or wordParse[i] == 'about' or wordParse[i] == 'not' or wordParse[i] == 'a'  or wordParse[i] == 'it'  or wordParse[i] == 'of'  or wordParse[i] == 'and' or wordParse[i] == 'but' or wordParse[i] == 'into' or wordParse[i] == 'in' or wordParse[i] == 'only' or wordParse[i] == 'at' or wordParse[i] == 'any' or wordParse[i] == 'you' or wordParse[i] == 'are' or wordParse[i] == 'does' or wordParse[i] == "don't" or wordParse[i] == "doesn't" or wordParse[i] == "can't" or wordParse[i] == 'are':

	# 			synPhrase = synPhrase + " " + wordParse[i]		

	# 		else: 

	# 			synPhrase = synPhrase + " " + random.choice(synonyms) #was randSyn from line 51

print quotesOnly

# print synPhrase + '\n' + '\n' + cleanser  #-----more than 140 characters

# for y in range(0,100000):
# 	api.update_status(synPhrase)
# 	time.sleep(120)


#=======splits into 1 quote ea. lists divided by word
#=======for x in range(0, (len(quotesOnly))):

#======= 	wordParse = quotesOnly[x].split(" ")


# dealing with capital first letters:
	#convertLowercase = wordParse.lower() 
	#convertUppercase = synPhrase[0].upper()

# words to skip
	# articles = ['a', 'an', 'the',]

	# pronouns = ['I', 'you', 'he', 'she', 'it', 'we', 'they']

	# conjunctions = ['and', 'or', 'but', 'so', 'yet']

	# simpleVerbs = ['am', 'are', 'is', 'have', 'has']

	# modalVerbs = ['can', 'might', 'do', 'not', 'its', 'could', 'would', 'should', 'have to', 'will']

	# contractions = ["don't", "it's", "won't", "aren't", "isn't", "doesn't", "you're", "I'm", "that's", "you'll", "they're", "there's", "who've", "can't", "didn't", "couldn't", "shouldn't", "wouldn't"]

	# prepositions = ['of', 'for', 'on', 'in', 'into', 'at', 'to', 'after', 'about', 'as', 'by', 'like', 'than', 'up', 'with']

	# questionWords = ['where', 'when', 'how', 'who', 'what', 'why']

	# random = ['nine-ninety', 'percent']

	# ..............WHAT ABOUT: possessive s: "'s"? and "'cause"

	# skipWords = articles + pronouns + conjunctions + simpleVerbs + modalVerbs + contractions + prepositions + questionWords	


	# for i in range(0, (len(wordParse))):

	# 	synonyms = dictionary.synonym(wordParse[i])

	# 	randSyn = random.choice(synonyms)


	# 	if wordParse[i] == skipWords:

	# 		synPhrase = synPhrase + " " + wordParse[i]		

	# 	else: synPhrase = synPhrase + " " + randSyn

	# print synPhrase


#ALSO WORKED for ADDING WORDS TO BE SKIPPED via IF STATEMENT
	
	#version 2
	# for i in range(0, (len(wordParse))):

	# 	synonyms = dictionary.synonym(wordParse[i])

	# 	randSyn = random.choice(synonyms)

	# 	if wordParse[i] == 'the' or wordParse[i] == 'to' or wordParse[i] == 'is':

	# 		synPhrase = synPhrase + " " + wordParse[i]		

	# 	else: synPhrase = synPhrase + " " + randSyn

	# print synPhrase

	#version 1
	# for i in range(0, (len(wordParse))):

	# 	synonyms = dictionary.synonym(wordParse[i])

	# 	randSyn = random.choice(synonyms)

	# 	if wordParse[i] == 'the':

	# 		synPhrase = synPhrase + " " + wordParse[i]

	# 	elif wordParse[i] == 'to':

	# 		synPhrase = synPhrase + " " + wordParse[i]	

	# 	elif wordParse[i] == 'is':

	# 		synPhrase = synPhrase + " " + wordParse[i]		

	# 	else: synPhrase = synPhrase + " " + randSyn

	# print synPhrase