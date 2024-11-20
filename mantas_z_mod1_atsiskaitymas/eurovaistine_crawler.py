import requests
from lxml.etree import HTML

def crawl_eurovaistine():
    url = "https://www.eurovaistine.lt/kosmetika"
    response = requests.get(url)
    text = response.text
    tree = HTML(text)

    products = tree.xpath(".//div[contains(@class, 'content')]")

    return [{
        "title": product.xpath(".//div[contains(@class, 'title']/text()")[0].strip(),
        "price": product.xpath(".//div[contains(@class, 'newProductPrice')]/text()")[0].strip()
    } for product in products][:4]

