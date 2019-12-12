import requests
from bs4 import BeautifulSoup
import csv

url = 'https://arc.lib.montana.edu/ojs/index.php/Young-Scholars-In-Writing/search/search'
searchTerms = ["meltin", "melting", "rhetori", "rhetoric", "politics", "politi", "justice", "justic"]
csvFileName = 'SearchResults.csv'

# Open CSV file
with open(csvFileName, 'w', newline='') as csvfile:
	# Setup header row
	fieldnames = ['Title', 'Authors', 'Pages', 'Published']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()


	for searchTerm in searchTerms:
		print("Searching with term \'{}\'...".format(searchTerm))
		# Get search result webpage
		query = requests.post(url, {'query' : searchTerm})
		instance = BeautifulSoup(query.text, 'html.parser')
		# Find all title <div> and their meta info
		titles = instance.findAll('div', {'class' : 'title'})
		metaData = instance.findAll('div', {'class' : 'meta'})
		print("\t{} results found".format(len(titles)))
		
		# Iterate over titles and metaData simultaneously
		for (titleDiv, metaDiv) in zip(titles, metaData):
			# Get the field values for each tag
			title 		= titleDiv.find('a')
			authors 	= metaDiv.find('div', {'class' : 'authors'})
			pages 		= metaDiv.find('div', {'class' : 'pages'})
			published 	= metaDiv.find('div', {'class' : 'published'})
		
			# Write the row
			writer.writerow(
				{
					'Title' : 'Unkown' if (title == None) else title.contents[0].strip(),
					'Authors' : 'Unkown' if (authors == None) else authors.contents[0].strip(),
					'Pages' : 'Unkown' if (pages == None) else pages.contents[0].strip(),
					'Published' : 'Unkown' if (published == None) else published.contents[0].strip()
				}
			)
	
print("Done! Open {} with Microsoft Excel or something similar to see the search results".format(csvFileName))