import requests
import bs4

url = 'https://arc.lib.montana.edu/ojs/index.php/Young-Scholars-In-Writing/search/search'
searchTerms = ["meltin", "melting", "rhetori", "rhetoric"]
obj = []
toRetrieve = []
instance = []
results = []

for i in range(len(searchTerms)):
    obj.append({'query': searchTerms[i]})
    toRetrieve.append(requests.post(url, data=obj[i]))
    instance.append(bs4.BeautifulSoup(toRetrieve[i].text, 'html.parser'))
    results.append(instance[i].findAll('div', {'class': 'obj_article_summary', 'class': 'title'}))
    print('Results for', searchTerms[i], ':', results[i])
