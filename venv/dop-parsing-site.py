import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 YaBrowser/19.4.0.2134 Yowser/2.5 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',}    #словарь, в которм будут заголовки ---- 'accept': '*/*'


def get_html(url, params=None):
    '''
    :param url: url страницы, с которой необходимо получить контент
    :param params: оптиональные параметр - доп. параметры(*передавать номера стр., чтобы спарсить все страницы марки)
    :return:
    '''
    r = requests.get(url,headers=HEADERS, params=params)
    return r

def parse():
    '''

    :return:
    '''
    html = get_html(URL)#парсим первую стр
    # print(html)#<Response [200]>
    # print(html.status_code)#200
    if html.status_code == 200:# все хорошо
        # print(html.text)#весь html код
        get_content(html.text)
    else:
        print('error')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')#'html.parser' - тип документа с которым мы работаем
    items = soup.find_all('a', class_="proposition_link")
    # print(items)
    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_="proposition_title" ).get_text(strip=True),
            'link': item.a.get('href'),
        })
    print(cars)

parse()