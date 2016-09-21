# -*- coding: utf-8 -*-

import random


frost = "Two roads diverged in a wood, and I, I took the one less traveled by, and that has made all the difference"


two = ['deuce', 'couple', 'double', 'pair']

roads = ['routes', 'arteries', 'avenues', 'ways', 'courses', 'pathways', 'thoroughfares']

diverged = ['diverged', 'deviated', 'strayed', 'veered']

wood = ['wood', 'timber', 'woodland', 'grove', 'thicket']

took = ['took', 'chose', 'drew', 'picked', 'selected', 'elected']

less = ['less', 'lesser', 'minorly', 'inferiorly', 'fewer']

traveled = ['traveled', 'crossed', 'migrated', 'proceeded', 'roamed', 'sailed', 'toured','trekked', 'visited', 'walked', 'wandered']

made = ['made', 'caused', 'formed', 'generated', 'manufactured', 'begotten', 'constructed', 'engendered', 'fashioned', 'forged', 'shaped']

difference = ['difference', 'variation', 'distortion', 'divergence']


#frost_reworked = 

print random.choice (two) + " " + random.choice (roads)+ " " + random.choice (diverged) + " in a " + random.choice (wood) + ", and I, I " + random.choice (took) + " the one " + random.choice (less) + " " + random.choice (traveled) + " by, and that has " + random.choice (made) + " all the " + random.choice (difference)