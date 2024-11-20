import requests
from xml.etree import HTML

def crawl_eurovaistine(url: str):
    response = requests.get(url)
    text = response.text
    tree = HTML(text)

