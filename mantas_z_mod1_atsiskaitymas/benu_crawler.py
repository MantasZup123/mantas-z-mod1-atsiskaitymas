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

    titles = tree.xpath("//h2[contains(@class, 'h3')]/text()")
    prices = tree.xpath("//span[contains(@class, 'money_amount')]/text()")

    return {"titles": titles, "prices": prices}

print(crawl_benu())


