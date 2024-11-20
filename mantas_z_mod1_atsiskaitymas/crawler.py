import requests
import time
from eurovaistine_crawler import crawl_eurovaistine
from benu_crawler import crawl_benu

def crawl(time_limit: int = 60, source: str, data_format: str = "json"):


