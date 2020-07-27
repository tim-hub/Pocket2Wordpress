import datetime

import requests

from worker.settings import POCKET_URL, ACCESS_TOKEN, CONSUMER_KEY

from typing import List


def get_articles() -> List:
    pocket_url = '{}?consumer_key={}&access_token={}'.format(POCKET_URL, CONSUMER_KEY, ACCESS_TOKEN)
    ts = (datetime.datetime.now() - datetime.timedelta(days=7)).timestamp()
    url = '{}&since={}'.format(pocket_url, ts)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['list']
    else:
        raise Exception('Cannot fetch articles')
