# -- coding: utf-8 --

from PyDictionary import PyDictionary

import random 

dictionary=PyDictionary()


frost = ['Two', 'roads', 'diverged', 'in', 'a', 'wood', ',', 'and', 'I', ',', 'I', 'took', 'the', 'one', 'less', 'traveled', 'by', 'and', 'that', 'has', 'made', 'all', 'the', 'difference']

print random.choice((dictionary.synonym(frost[0]))) + " " + random.choice((dictionary.synonym(frost[1]))) + " " + random.choice((dictionary.synonym(frost[2]))) + " " + frost[3] + " " + frost[4] + " " + random.choice((dictionary.synonym(frost[5]))) + ","

