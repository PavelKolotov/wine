import datetime
import pandas
import argparse


from collections import defaultdict
from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from environs import Env


FOUNDATION_YEAR = 1920


def get_age_name(year):
    num_years = int(str(year)[-2:])
    if num_years < 21 and num_years > 4 or int(str(num_years)[-1:]) == 0:
        return 'лет'
    elif int(str(num_years)[-1:]) == 1:
        return 'год'
    else:
        return 'года'


def main():
    env = Env()
    env.read_env()
    file_path = env('FILE_PATH')
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', default=file_path)
    args = parser.parse_args()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    winery_age_now = datetime.datetime.now().year - FOUNDATION_YEAR
    excel_data_df = pandas.read_excel(args.file_path, na_values='nan', keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    template = env.get_template('template.html')
    wines_categories = defaultdict(list)

    for wine in wines:
        wine_category = list(wine.keys())[0]
        wines_categories[wine[wine_category]].append(wine)

    rendered_page = template.render(
        wines=wines_categories,
        winery_age=winery_age_now,
        age_name=get_age_name(winery_age_now),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
