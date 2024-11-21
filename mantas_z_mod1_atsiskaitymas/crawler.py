import requests
import time
from eurovaistine_crawler import crawl_eurovaistine
from benu_crawler import crawl_benu

def crawl(time_limit: int = 60, url: str, data_format: str = "json"):
    start_time = time.time()

    if url == "eurovaistine":
        data = crawl_eurovaistine()
    elif url == "benu":
        data = crawl_benu()
    else:
        raise ValueError("Tokios svetainės nucrawlinti negalime")




