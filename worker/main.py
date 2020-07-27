# from app import pocket_api as api
#
# articles = api.get_articles()
#
# import json
#
# with open('tests/unit/sample.json', 'w') as file:
#     file.write(
#         json.dumps(articles)
#     )

# from worker import wordpress_api
#
# r= wordpress_api.fetch_posts()
# print(r)
from datetime import datetime

from utils.read_sample_articles import read_all
from worker.formatter import format_all
from worker.pocket_api import get_articles
from worker.settings import PYTHON_ENV
from worker.wordpress_api import create_a_post


def main():
    # get artciles
    if (PYTHON_ENV == 'development'):
        articles = read_all()

    else:
        articles = get_articles()

    # format content to html

    currentDate = datetime.now().strftime("%Y-%m-%d")
    title = '''Weekly technology update {}'''.format(currentDate)
    htmlContent = format_all(articles.items(), title)
    # print(htmlContent)

    # post to wordpress as a new post

    create_a_post(
        {
            'content': htmlContent,
            'title': title,
            'status': 'publish',
            'slug': title
        }
    )

    return
