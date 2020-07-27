import random
from typing import List

from jinja2 import Template


def jinja_format(articles: List):
    template = Template(open('./templates/article.jinja').read())

    return template.render(
        articles=articles,
        minutes=random.choice(list(range(3, 8, 1)))
    )

