import requests
from bs4 import BeautifulSoup


payload = {'k':'mobile'}
response = requests.get('https://www.amazon.in/s', params=payload)
html_soup = BeautifulSoup(response.text,'html.parser')
mobile_containers = html_soup.find_all('div', class_='a-section a-spacing-medium')
print(mobile_containers)


names = []
ratings = []
saling_prices = []
actual_prices = []
images = []

for container in mobile_containers:
    print("hh")
    name = container.find('span', class_='a-size-medium a-color-base a-text-normal')
    saling_price = container.find('span', class_ ='a-price-whole')
    rating = container.find('span', class_ ='a-icon-alt')
    actual_price = container.find('span', class_ ='a-offscreen')
    # image = container.find('div', class_='a-section aok-relative s-image-fixed-height')
    if name is not None:
        name = name.text
        names.append(name)

    if saling_price is not None:
        saling_price = saling_price.text
        saling_prices.append(saling_price)

    if actual_price is not None:
        actual_price = actual_price.text
        actual_prices.append(actual_price)

    if rating is not None:
        rating = rating.text
        ratings.append(rating)

    # if image is not None:
    #     image = (image.img['src'])
    #     images.append(image)


# for im in images:
#     print(im)

print(len(names))
print(len(saling_prices))
print(len(actual_prices))
print(len(ratings))
# print(len(images))
#