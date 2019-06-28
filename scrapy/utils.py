import requests
from bs4 import BeautifulSoup

from .models import ScrappedData


def scrap_amazon(param):
    payload = {'k': param}
    response = requests.get('https://www.amazon.in/s', params=payload)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    mobile_containers = html_soup.find_all('div', class_='a-section a-spacing-medium')

    amazon_list = []

    for container in mobile_containers:
        name = container.find('span', class_='a-size-medium a-color-base a-text-normal')
        selling_price = container.find('span', class_='a-price-whole')
        rating = container.find('span', class_='a-icon-alt')
        actual_price = container.find('span', class_='a-offscreen')
        image = container.find('div', class_='a-section aok-relative s-image-fixed-height')

        if name and selling_price and actual_price and rating and image:
            amazon = {
                'name': name.text,
                'selling_price': selling_price.text,
                'actual_price': actual_price.text,
                'rating': rating.text,
                'image': image.img['src']
            }

            amazon_list.append(ScrappedData(**amazon))

    for item in amazon_list:
        print(item)

    return amazon_list


def scrap_flipkart(param):
    payload = {'q': param}
    response = requests.get('http://www.flipkart.com/search', params=payload)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    mobile_containers = html_soup.find_all('div', class_='_1UoZlX')

    flipkart = {}
    flipkart_list = []

    for container in mobile_containers:
        name = container.find('div', class_='_3wU53n')
        selling_price = container.find('div', class_='_1vC4OE _2rQ-NK')
        actual_price = container.find('div', class_='_3auQ3N _2GcJzG')
        rating = container.find('div', class_='hGSR34')
        image = container.find('div', class_='_3BTv9X')

        if name and selling_price and actual_price and rating and image:
            flipkart = {
                'name': name.text,
                'selling_price': selling_price.text,
                'actual_price': actual_price.text,
                'rating': rating.text,
                'image': image.img['src']
            }
            flipkart_list.append(ScrappedData(**flipkart))

    for item in flipkart_list:
        print(item)

    return flipkart_list;




