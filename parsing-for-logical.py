from bs4 import BeautifulSoup
import urllib.request

#
url = 'https://cmsmagazine.ru/journal/items-80-problems-with-it-interviews/'
req = urllib.request.urlopen(url)
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

all = soup.find_all('div', class_="_3mS9ZqXt6a")
# print(all)
res = []
punkt = ''

for item in all:
    punkt = item.find('p').get_text(strip=True)
    answer = item.find('div', class_='answer_text').get_text(strip=True)
    # print(answer)
    # print(punkt)
    res.append({
        'punkt': punkt,
        'answer': answer,
    })
#
print(res)
# print(num_of_z)
# # '''
# news = soup.find_all('li', class_='liga-news-item')
# # print(news)
#
# results = []# хранение результата данных (список словарей)
#
# for item in news:
#     title = item.find('span', class_="fz-16 fw-500 d-block").get_text(strip=True)#возвращаем строку и только текст между тегами
#     # print(title)
#     desc = item.find('span', class_="name-dop").get_text(strip=True)
#     # print(desc)
#     href = item.a.get('href')# можем указывать теги - сейчас ткг а - и у данного тега нам нужен href
#     # print(href)
#     results.append({
#         'title': title,
#         'desc': desc,
#         'href': href,
#     })
# print(results)
#
# f = open('news.txt', 'w', encoding='utf-8')
# i = 1
# for item in results:
#     f.write(f'Новость {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n\n')
#     i+=1
# f.close()