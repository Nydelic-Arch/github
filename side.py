import requests
from bs4 import BeautifulSoup


def quick_get(url) -> BeautifulSoup:
    rq = requests.get(url)
    return BeautifulSoup(rq.text, "lxml")


import re


def has_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))
