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

    products = tree.xpath("//a[contains(@class, 'productCard')]")

    return[{
        "Title": product.xpath(".//div[contains(@class, 'title')]/span/text()")[0].strip(),
        "Price": product.xpath(".//div[contains(@class, 'newProductPrice')]/span/text()")[0].strip()
    } for product in products]

#print(crawl_eurovaistine())