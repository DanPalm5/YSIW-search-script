import requests
from bs4 import BeautifulSoup

url = 'https://arc.lib.montana.edu/ojs/index.php/Young-Scholars-In-Writing/search/search'
searchTerms = ["meltin", "melting", "rhetori", "rhetoric", "politics", "politi", "justice", "justic"]

for searchTerm in searchTerms:
	results = BeautifulSoup(requests.post(url, {'query': searchTerm}).text, 'html.parser').findAll('div', {'class': 'title'})
	print('Results for', searchTerm, ':')
	print(len(results), 'articles for', searchTerm, ':', '\n')
	for result in results:
		print('\t', result.find('a').contents[0].strip(), '\n')