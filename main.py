import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


rendered_page = template.render(
    wine1_img='images/hvanchkara.png',
    wine1_name='Хванчкара',
    wine1_grape_sort='Александраули',
    wine1_price='550 р.',
    wine2_img='images/rkaciteli.png',
    wine2_name='Ркацители',
    wine2_grape_sort='Ркацители',
    wine2_price='499 р.',
    wine3_img='images/belaya_ledi.png',
    wine3_name='Белая леди',
    wine3_grape_sort='Дамский пальчик',
    wine3_price='399 р.',
    wine4_img='images/izabella.png',
    wine4_name='Изабелла',
    wine4_grape_sort='Изабелла',
    wine4_price='350 р.',
    wine5_img='images/granatovyi_braslet.png',
    wine5_name='Гранатовый браслет',
    wine5_grape_sort='Мускат розовый',
    wine5_price='350 р.',
    wine6_img='images/shardone.png',
    wine6_name='Шардоне',
    wine6_grape_sort='Шардоне',
    wine6_price='350 р.',
    winery_age=datetime.datetime.now().year - 1920

)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
