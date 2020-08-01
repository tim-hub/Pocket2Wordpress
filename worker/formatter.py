import os
import random
from datetime import datetime
from typing import List, Dict

from jinja2 import Template

from worker.settings import WP_CAT_ID, WP_TAG_ID


class Render:
    def __init__(self, articles: List):
        self.articles = articles
        currentDate = datetime.now().strftime("%d %b, %Y")
        self.title = '''Technology Reading Update (weekly) - {}'''.format(currentDate)
        self.reading_minutes = random.choice(list(range(3, 8, 1)))

        self.set_excerpt()
        self.set_image()

    def set_excerpt(self):
        part1 = self.articles[0][1]['excerpt'] if self.articles[0][1]['excerpt'] else ''
        part2 = self.articles[-1][1]['excerpt'] if self.articles[-1][1]['excerpt'] else ''
        self.excerpt = part1 + part2

    # set image not work yet todo
    def set_image(self):
        return

    def jinja_format(self) -> str:
        current_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(current_path, './templates/article.jinja')
        template = Template(open(path).read())
        return template.render(
            articles=self.articles,
            minutes=self.reading_minutes
        )

    def get_wp_post_body(self) -> Dict:
        title = self.title
        htmlContent = self.jinja_format()
        # print(htmlContent)

        return {
            'content': htmlContent,
            'title': '⭐️ ' + title,
            'status': 'publish',
            'slug': title,  # wordpress will slugify automatically
            #     'excerpt': '''
            # {} -- {}, this is tim's weekly digest through pocket application.
            # This article only contains high quality technology, news, programming, architecture and geek stuff.
            # More high quality content is on my blog https://tim.bai.uno.
            #
            #     '''.format(self.excerpt, title),
            'categories': [WP_CAT_ID],
            'tags': [WP_TAG_ID],

        }
