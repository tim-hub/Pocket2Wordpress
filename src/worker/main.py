from src.utils import read_all
from src.worker.formatter import Render
from src.worker import get_articles
from src.worker import PYTHON_ENV
from src.worker.wordpress_api import create_a_post


def main():
    # get artciles
    if (PYTHON_ENV == 'development'):
        articles = read_all()

    else:
        articles = get_articles(7)

    # format content to html and get post body

    render = Render(list(articles.items()))

    # post to wordpress as a new post

    create_a_post(render.get_wp_post_body())

    return
