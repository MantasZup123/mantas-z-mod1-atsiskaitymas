import requests
from lxml.etree import HTML

def crawl_eurovaistine():
    url = "https://www.eurovaistine.lt/?utm_source=google&utm_medium=cpc&utm_campaign=%5BEV%20BRAND%5D%20-%20Eurovaistine&utm_id=1543031168&gbraid=0AAAAADRyq90KMHdmqbBcDjCO3L_MPjcFR&gclid=CjwKCAiArva5BhBiEiwA-oTnXR3GzX33oBWvrvMvSA4dtonpaovb2NwxqzrsJ44CFAvSJsjOLQrcehoCJsYQAvD_BwE"
    response = requests.get(url)
    text = response.text
    tree = HTML(text)

    products = tree.xpath(".//div[contains(@class, 'content')]")

    return [{
        "title": product.xpath(".//div[contains(@class, 'title']/text()")[0].strip(),
        "price": product.xpath(".//div[contains(@class, 'newProductPrice')]/text()")[0].strip()
    } for product in products][:4]

