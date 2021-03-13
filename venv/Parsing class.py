from update_parsing import ParsingMy
from Parser_class import Parser

parser = Parser('https://www.ua-football.com/sport', 'news.txt')
parser.run()
# print(parser.raw_html)
# print(parser.html)
# print(parser.results)



url = 'https://www.ua-football.com/sport'
pars = ParsingMy(url)
pars.get_news()
pars.parsing()
pars.write_to_file('parsingOOP.txt')