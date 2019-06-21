from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
html_soup = BeautifulSoup(response.text,'html.parser')
movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
print(len(movie_containers))
print(type(html_soup))

names = []
years = []
imdb_ratings = []
metascores = []
votes = []
# Extract data from individual movie container
for container in movie_containers:
# If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
# The name
	    name = container.h3.a.text
	    names.append(name)
	# The year
	    year = container.h3.find('span', class_ = 'lister-item-year').text
	    years.append(year)
	# The IMDB rating
	    imdb = float(container.strong.text)
	    imdb_ratings.append(imdb)
	# The Metascore
	    m_score = container.find('span', class_ = 'metascore').text
	    metascores.append(int(m_score))
	# The number of votes
	    vote = container.find('span', attrs = {'name':'nv'})['data-value']
	    votes.append(int(vote))


test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(test_df.info())
print(test_df)	    