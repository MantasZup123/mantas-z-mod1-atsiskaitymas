import requests
from lxml.etree import HTML

def crawl_benu():
    """
    Function reads data from benu website
    :param source: Websites URL
    :return: Data received - titles and prices
    """
    source = "https://www.benu.lt/menesio-top-pasiulymai?vars/gclid/CjwKCAiArva5BhBiEiwA-oTnXX6Umbk0M9UK8rG2G6UbnWgJeXX6HH_C4oWWtSg4vIZXSEvkmGTTPxoCZvgQAvD_BwE"
    response = requests.get(source)
    text = response.text
    tree = HTML(text)

    products = tree.xpath(".//div[contains(@class, 'bnProductCard')]")

    return [{
        "title": tree.xpath(".//div[contains(@class, 'bnProductCard__title')]/text()")[0].strip(),
        "price": tree.xpath(".//div[contains(@class, 'money_amount')]/text()")[0].strip(),
    } for product in products][:4]
