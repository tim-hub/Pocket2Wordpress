import requests
from requests.auth import HTTPBasicAuth

from app.settings import WP_URL, WP_APP_PWD, WP_USER

# wordpress api posts
# https://developer.wordpress.org/rest-api/reference/posts/#create-a-post


POSTS_URL = '{}/wp-json/wp/v2/posts'.format(WP_URL)


def create_a_post(data):
    resp = requests.post(POSTS_URL, data=data, auth=HTTPBasicAuth(WP_USER, WP_APP_PWD))
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception('Cannot create an article')


def fetch_posts():
    resp = requests.get(POSTS_URL, auth=HTTPBasicAuth(WP_USER, WP_APP_PWD))
    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception('Cannot fetch articles from wordpress')
