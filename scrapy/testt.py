import requests
from bs4 import BeautifulSoup

payload = {'q': 'mobile'}
response = requests.get('http://www.flipkart.com/search', params=payload)
html_soup = BeautifulSoup(response.text, 'html.parser')
mobile_containers = html_soup.find_all('div', class_='_1UoZlX')

flipkart_list = []

for container in mobile_containers:
    name = container.find('div', class_='_3wU53n')
    selling_price = container.find('div', class_='_1vC4OE _2rQ-NK')
    actual_price = container.find('div', class_='_3auQ3N _2GcJzG')
    rating = container.find('div', class_='hGSR34')
    image = container.find('div', class_='_3BTv9X')
    link = container.find('div', class_ ='_31qSD5')
    print('hh')
    if name and selling_price and actual_price and rating and image and link:
        print('hh')
        # flipkart = {
        #     'keyword': param,
        #     'name': name.text,
        #     'source': FLIPKART,
        #     'selling_price': float(selling_price.text.replace('₹', '').replace(',', '').replace(' ', '')),
        #     'actual_price': float(actual_price.text.replace('₹', '').replace(',', '').replace(' ', '')),
        #     'rating': rating.text,
        #     'image': image.img['src']
        # }
        print('hh')
        flipkart_list.append(name.txt)

print(len(flipkart_list));