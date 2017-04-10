#!usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

mainpage = "https://www.olx.ua/nedvizhimost/prodazha-kvartir/novostroyki/kiev/"

def get_html(url):
    f = urllib.request.urlopen(url)
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

def get_page_data(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_='content')
#    name = data.find('h1').text.strip()
#    district = data.find('a', class_='show-map-link').text.strip()
    descrcont = data.find('table', class_='details fixed marginbott20 margintop5 full').find_all('strong')[2:]
#    rooms = descrcont[0].text.strip()
#    square = descrcont[1].text.strip()
#    life_square = descrcont[2].text.strip()
#    kitchen_square = descrcont[3].text.strip()
#    floor = descrcont[4].text.strip()
#    max_floor = descrcont[5].text.strip()
    info = data.find('p', class_='pding10 lheight20 large').text.strip()
    data2 = data.find('em').text.strip()
#    time = data2.split("Добавлено: ")[-1].split('в ')[-1].split(', Номер объявления: ')[0]
#    number = data2.split("Добавлено: ")[-1].split('в ')[-1].split(', Номер объявления: ')[1]
#    views = data.find_all('div', 'pdingtop10')[1].text.split('Просмотры:')[-1].strip()
    dataset=({
    'name': data.find('h1').text.strip(),
    'district': data.find('a', class_='show-map-link').text.strip(),
    'rooms': descrcont[0].text.strip(),
#    'square': descrcont[1].text.strip(),
#    'life_square': descrcont[2].text.strip(),
#    'kitchen_square': descrcont[3].text.strip(),
#    'floor': descrcont[4].text.strip(),
#    'max_floor': descrcont[5].text.strip(),
    'time': data2.split("Добавлено: ")[-1].split('в ')[-1].split(', Номер объявления: ')[0],
    'number': data2.split("Добавлено: ")[-1].split('в ')[-1].split(', Номер объявления: ')[1],
    'views': data.find_all('div', 'pdingtop10')[1].text.split('Просмотры:')[-1].strip()
    })
    return(dataset)

def main():
    data = []
    for url in get_urls_from_mainpage(get_html(mainpage)):
        data.append(get_page_data(url))
    f = open('/home/ihor/course/apartaments.txt', 'w')
    for line in data:
        f.write(str(line)+'\n')
    f.close()

if __name__ == '__main__':
    main()
