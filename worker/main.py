
from datetime import datetime

from utils.read_sample_articles import read_all
from worker.formatter import jinja_format
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

    currentDate = datetime.now().strftime("%d %b, %Y")
    title = ''' Technology Reading Update (weekly) - {}'''.format(currentDate)
    # htmlContent = format_all(articles.items(), title)

    htmlContent = jinja_format(articles.items())
    print(htmlContent)
    # post to wordpress as a new post

    create_a_post(
        {
            'content': htmlContent,
            'title': title,
            'status': 'publish',
            'slug': title,
            'excerpt': '''
{}, this is what I read this week through pocket application.
This article only contains high quality technology, news, programming, architecture and geek stuff.
More high quality content is on my blog https://tim.bai.uno. 
The source code is at https://github.com/tim-hub
               
            '''.format(title),
            'categories': [21],
            'tags': [22],
        }
    )

    return
