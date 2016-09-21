# -*- coding: utf-8 -*-

from PyDictionary import PyDictionary

from random import randint

dictionary=PyDictionary()

#import twitter
#api = twitter.Api(consumer_key='',
                      #consumer_secret='',
                      #access_token_key='',
                      #access_token_secret='')

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