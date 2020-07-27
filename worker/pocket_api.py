import datetime
from typing import List

import requests

from worker.settings import POCKET_URL, ACCESS_TOKEN, CONSUMER_KEY


def get_articles(days: int = 7) -> List:
    pocket_url = '{}?consumer_key={}&access_token={}'.format(POCKET_URL, CONSUMER_KEY, ACCESS_TOKEN)
    ts = (datetime.datetime.now() - datetime.timedelta(days=days)).timestamp()
    url = '{}&since={}'.format(pocket_url, ts)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['list']
    else:
        raise Exception('Cannot fetch articles')
