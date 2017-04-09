#!usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

mainpage = "https://www.olx.ua/nedvizhimost/prodazha-kvartir/novostroyki/kiev/"

def get_html(url):
    f = urllib.request.urlopen(mainpage)
    return f.read()

def get_urls_from_mainpage(html):
    urls = []
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', class_= 'fixed offers breakword ')
    rows = table.find_all('tr', 'wrap')
    for row in rows:
        a = row.find_all('a', class_='marginright5 link linkWithHash detailsLink')
        urls.append(str(a).split('<a class="marginright5 link linkWithHash detailsLink" href="')[-1].split('">')[0])

    return urls
def main():
    print(get_urls_from_mainpage(get_html(mainpage)))

if __name__ == '__main__':
    main()
