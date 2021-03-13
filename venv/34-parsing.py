from bs4 import BeautifulSoup
import urllib.request

'''
рекоендуется делать в виде функций
1. сделать запрос = urllib.request.urlopen()
2. прочтем содержимое нашего ответа = req.read()
'''
req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()

soup = BeautifulSoup(html, 'html.parser') # получаем читабельный html-код
# print(soup)
news = soup.find_all('li', class_='liga-news-item')
# print(news)

results = []# хранение результата данных (список словарей)

for item in news:
    title = item.find('span', class_="fz-16 fw-500 d-block").get_text(strip=True)#возвращаем строку и только текст между тегами
    # print(title)
    desc = item.find('span', class_="name-dop").get_text(strip=True)
    # print(desc)
    href = item.a.get('href')# можем указывать теги - сейчас ткг а - и у данного тега нам нужен href
    # print(href)
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })
print(results)

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n\n')
    i+=1
f.close()