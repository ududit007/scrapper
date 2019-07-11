from django.core.management.base import BaseCommand

from scrapy.models import ScrappedData
from scrapy.utils import scrap_amazon, scrap_flipkart

keys = []


def update_data():
    all_data = []
    amazon_list = []
    flipkart_list = []
    for key in keys:
        amazon_list += scrap_amazon(key)
        flipkart_list += scrap_flipkart(key)

    for flipkart_dict in flipkart_list:
        all_data.append(ScrappedData(**flipkart_dict))

    for amazon_dict in amazon_list:
        all_data.append(ScrappedData(**amazon_dict))

    ScrappedData.objects.bulk_create(all_data)


class Command(BaseCommand):
    # scrap_data = ScrappedData.objects.values('keyword').distinct()
    # for data in scrap_data:
    #     keys.append(data)

    def handle(self, *args, **options):
        update_data()