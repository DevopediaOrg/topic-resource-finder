import requests

user_search = input('search keyword: ')
user_search = user_search.replace(' ','+')

#books search
url = 'https://openlibrary.org/search.json?q='
data = requests.get(url+user_search).json()
for i in range(len(data['docs'])):
	try:
		print(data['docs'][i]['title_suggest'],' - ',data['docs'][i]['author_name'])
	except:
		pass