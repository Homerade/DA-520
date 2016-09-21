# -*- coding: utf-8 -*-

totc_opener = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way–in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

a_count = totc_opener.count('a')
e_count = totc_opener.count('e') 
i_count = totc_opener.count('i')
o_count = totc_opener.count('o')
u_count = totc_opener.count('u')

vowel_count = a_count + e_count + i_count + o_count + u_count

clean_text = totc_opener.replace(' ','').replace(',','').replace('-','').replace('.','')

letter_count = 	len(clean_text)

percent = (vowel_count * 100)/letter_count

print("Vowels account for " + str(percent) + "% of the first paragraph.")


