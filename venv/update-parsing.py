from bs4 import BeautifulSoup
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')

        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

class ParsingMy:

    def __init__(self, url):
        self.url = url
        self.result = []
        self.news = []

    def get_news(self):
        req = urllib.request.urlopen(url)
        html = req.read()
        soup = BeautifulSoup(html, 'html.parser')
        news = soup.find_all('li', class_= 'liga-news-item')
        self.news = news
        return self.news

    def parsing(self):
        results = []
        for item in self.news:
            title = item.find('span', class_="fz-16 fw-500 d-block").get_text(
                strip=True)  # возвращаем строку и только текст между тегами
            # print(title)
            desc = item.find('span', class_="name-dop").get_text(strip=True)
            # print(desc)
            href = item.a.get('href')  # можем указывать теги - сейчас ткг а - и у данного тега нам нужен href
            # print(href)
            results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })
        print(results)
        self.result = results
        return self.result

    def write_to_file(self, file):
        file = open(file,'w', encoding='utf-8')
        i = 1
        for item in self.result:
            file.write(
                f'Новость {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n\n')
            i += 1
        file.close()
        return 'successful'
