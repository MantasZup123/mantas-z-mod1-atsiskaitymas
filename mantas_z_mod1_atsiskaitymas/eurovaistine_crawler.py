import requests
from lxml.etree import HTML

def crawl_eurovaistine():
    """
    Function reads data from eurovaistine website
    :param source: Websites URL
    :return: Data received - titles and prices
    """
    source = "https://www.eurovaistine.lt/kosmetika"
    response = requests.get(source)
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'productsListWrapper__cardsContainer')]")

    return [{
        "title": product.xpath(".//div[contains(@class, 'title')]/span/text()")[0].strip(),
        "price": product.xpath(".//div[contains(@class, 'newProductPrice')]/span/text()")[0].strip()
    } for product in products][:4]

print(crawl_eurovaistine())