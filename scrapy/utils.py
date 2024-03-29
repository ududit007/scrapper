import random
import requests
from bs4 import BeautifulSoup

from .constants import AMAZON, FLIPKART, USER_AGENTS, PROXY

agent = {
    "User-Agent": random.choice(USER_AGENTS),
    'Content-Type': 'application/json',
}
proxy = {'http': 'http://'+random.choice(PROXY)}


def remove_symbol(price):
    return float(price.text.replace('₹', '').replace(',', '').replace(' ', ''))


def scrap_amazon(param):
    payload = {'k': param}
    response = requests.get('https://www.amazon.in/s', headers=agent, proxies=proxy, params=payload)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    mobile_containers = html_soup.find_all('div', class_='a-section a-spacing-medium')

    amazon_list = []

    for container in mobile_containers:
        name = container.find('span', class_='a-size-medium a-color-base a-text-normal')
        selling_price = container.find('span' , class_='a-price-whole')
        rating = container.find('span', class_='a-icon-alt')
        actual_price = container.find('span', class_='a-offscreen')
        image = container.find('div', class_='a-section aok-relative s-image-fixed-height')

        if name and selling_price and actual_price and rating and image and container:
            amazon = {
                'keyword': param,
                'name': name.text,
                'source': AMAZON,
                'selling_price': remove_symbol(selling_price),
                'actual_price': remove_symbol(actual_price),
                'rating': rating.text,
                'image': image.img['src'],
                'link_product': container.a['href']
            }

            amazon_list.append(amazon)

    return amazon_list


def scrap_flipkart(param):
    payload = {'q': param}
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
        link = container.find('div', class_='_1UoZlX')

        if name and selling_price and actual_price and rating and image and container:
            flipkart = {
                'keyword': param,
                'name': name.text,
                'source': FLIPKART,
                'selling_price': remove_symbol(selling_price),
                'actual_price': remove_symbol(actual_price),
                'rating': rating.text,
                'image': image.img['src'],
                'link_product': container.a['href']
            }
            flipkart_list.append(flipkart)

    return flipkart_list


def scrap_flipkart2(param):
    payload = {'q': param}
    response = requests.get('http://www.flipkart.com/search', params=payload)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    mobile_containers = html_soup.find_all('div', class_='_3liAhj _1R0K0g')

    flipkart_list = []

    for container in mobile_containers:
        name = container.find('a', class_='_2cLu-l')
        selling_price = container.find('div', class_='_1vC4OE')
        actual_price = container.find('div', class_='_3auQ3N')
        rating = container.find('div', class_='hGSR34')
        image = container.find('div', class_='_3BTv9X')
        link = container.find('a', class_='Zhf2z-')

        if name and selling_price and actual_price and rating and image and container:
            flipkart = {
                'keyword': param,
                'name': name.text,
                'source': FLIPKART,
                'selling_price': remove_symbol(selling_price),
                'actual_price': remove_symbol(actual_price),
                'rating': rating.text,
                'image': image.img['src'],
                'link_product': container.a['href']
            }
            flipkart_list.append(flipkart)

    return flipkart_list

