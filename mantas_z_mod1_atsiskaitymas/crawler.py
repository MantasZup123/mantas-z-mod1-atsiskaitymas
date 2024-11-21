import requests
import json
import csv
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
        raise ValueError("Neturime prieigos prie šios svetainės.")

    if time.time() - start_time > time_limit:
        raise TimeoutError("Funkcijos veikimo laikas baigėsi.")

    if data_format == "json":
        data_json = json.loads(data)
        return data_json
    elif data_format == "csv":
        with open("data_csv.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price"])
            for title, price in data["titles"], data["prices"]:
                writer.writerow([title, price])
        return "Duomenys išsaugoti į data_csv.csv failą"
    elif data_format == "dict":
        return data
    else:
        raise ValueError("Toks formatamas yra nepalaikomas.")






