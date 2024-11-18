import requests
from json2html import *


FIELDS = ['id', 'title', 'description', 'category', 'price',
          'discountPercentage', 'rating', 'stock', 'tags', 'sku']


def get_fields(product):
    return {k: product[k] for k in FIELDS}


if __name__ == '__main__':
    BASE_URL = 'https://dummyjson.com'

    url = f'{BASE_URL}/products'
    response = requests.get(url=url)
    data = response.json()

    products = list(map(get_fields, data['products']))

    parsed_html = json2html.convert(json=products)

    with open('../outputs/output_6.html', 'w', encoding='utf-8') as output_file:
        output_file.write(parsed_html)
