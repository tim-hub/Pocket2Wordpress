from enum import Enum

from src.utils.read_sample_articles import read_all
from src.worker.formatter import Render
from src.worker.pocket_api import get_articles
from src.settings import PYTHON_ENV
from src.worker.wordpress_api import create_a_post


class OutputMode(Enum):
    WP = 'WP'
    MD = 'MD'


def main(destination: OutputMode = OutputMode.WP):
    # get artciles
    if (PYTHON_ENV == 'development'):
        articles = read_all()

    else:
        articles = get_articles(7)

    # format content to html and get post body

    render = Render(list(articles.items()))

    if (destination == OutputMode.WP):
        # post to wordpress as a new post
        create_a_post(render.get_wp_post_body())
    elif (destination == OutputMode.MD):
        print(render.get_wp_post_body())

    return
