from bs4 import BeautifulSoup
import requests
from datetime import datetime


def parse():
    page = requests.get('https://python.org').content
    tree = BeautifulSoup(page, 'html.parser')
    header = tree.find(text='Upcoming Events').parent
    for li in header.parent.findAll('li'):
        print(datetime.fromisoformat(li.time['datetime']),
              li.a.text)


if __name__ == '__main__':
    parse()