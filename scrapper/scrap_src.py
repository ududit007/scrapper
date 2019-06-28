import requests
from bs4 import BeautifulSoup


payload = {'k':'mobile'}
response = requests.get('https://www.amazon.in/s', params=payload)
html_soup = BeautifulSoup(response.text,'html.parser')
mobile_containers = html_soup.find_all('div', class_='a-section a-spacing-medium')
print(mobile_containers)
for x in mobile_containers:
    name = x.find('div', class_='a-section aok-relative s-image-fixed-height')
    # name = container.find('img', class_='_1Nyybr _30XEf0')
    # print('aa')
    print(name.img['src'])
# print(html_soup.a.img['src'])
