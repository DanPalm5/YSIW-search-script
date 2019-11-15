import requests
import bs4
url = 'https://arc.lib.montana.edu/ojs/index.php/Young-Scholars-In-Writing/search/search'
searchTerms = ["meltin", "melting", "rhetori", "rhetoric", "justice", "justic"]  # the terms we want to search for
obj = []   # creates a dictionary of terms to pass to query
toRetrieve = []  # stores requests sent to website via POST
instance = []  # each instance of a request is parsed into a string
results = []  # stores the final string that we want to see

for i in range(len(searchTerms)):
    obj.append({'query': searchTerms[i]})
    toRetrieve.append(requests.post(url, data=obj[i]))
    instance.append(bs4.BeautifulSoup(toRetrieve[i].text, 'html.parser'))
    results.append(instance[i].findAll('div', {'class': 'obj_article_summary', 'class': 'title'}))
    print('Results for', searchTerms[i], ':', results[i])  # shows us the results of search
    print("")
