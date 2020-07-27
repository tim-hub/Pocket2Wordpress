import random
from datetime import datetime
from functools import reduce
from typing import List, Tuple


def format_all(articles: List, title):
    top = '''
    <small> Continue reading takes about {minutes} minutes </small>
    '''.format(
        minutes=random.choice(list(range(3, 8, 1)))
    )

    content = reduce(
        lambda a, b: a + b,
        map(lambda args: format_one(args[0], args[1]), enumerate(articles))
    )

    bottom = '''
    <i>
        Thanks for your reading, save as your bookmark if you like my website.
    </i>
    '''

    return top + content + bottom


def format_one(index: int, articleTuple: Tuple, ):
    article = articleTuple[1]
    url = article['resolved_url']
    title = article['resolved_title']
    excerpt = article['excerpt']
    time_added = article['time_added']
    dt_added = datetime.fromtimestamp(int(time_added)).strftime("%Y-%m-%d")
    # time_to_read = article['time_to_read']
    image = article['top_image_url'] if 'top_image_url' in article else ''
    status = article['status']

    if title:
        return '''
        <div> 
            <a href='{url}' rel="nofollow">{index}. {title}</a> 
            <small> {date}</small>
            <p>
                {description}
            </p>
        </div>
        <hr/>
        '''.format(
            url=url,
            index=index + 1,
            title=title,
            date=dt_added,
            description=excerpt
        )
    else:
        return ''