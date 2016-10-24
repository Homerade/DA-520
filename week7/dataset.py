import csv
from pprint import pprint

file = open("immigration.csv")

data = csv.DictReader(file)

for row in data:
	print(row['Year'], row['Annual immigration into the United States: thousands. 1820 ? 1962'])

# import csv
# >>> with open('names.csv') as csvfile:
# ...     reader = csv.DictReader(csvfile)
# ...     for row in reader:
# ...         print(row['first_name'], row['last_name'])