from enum import Enum

from src.utils.read_sample_articles import read_all
from src.worker.formatter import Render
from src.worker.pocket_api import get_articles
from src.settings import PYTHON_ENV
from src.worker.wordpress_api import create_a_post

DIST_PATH = './dist/'


class OutputMode(str, Enum):
    WP = 'WP'
    MD = 'MD'


def main(destination):
    print(destination)
    print(destination == OutputMode.MD)
    # get artciles
    if (PYTHON_ENV == 'development'):
        articles = read_all()

    else:
        articles = get_articles(7)

    # format content to html and get post body

    render = Render(list(articles.items()))

    # save as markdowns
    md_obj = render.get_content_markdown()
    file_name = md_obj.get('file_name')
    content = md_obj.get('content')
    md_path = DIST_PATH + file_name + '.md'
    with open(md_path, 'w+') as file:
        file.write(content)

    if (destination == OutputMode.WP):
        # post to wordpress as a new post
        htmlBody = render.get_wp_post_body()
        create_a_post(htmlBody)

    return
