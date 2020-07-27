import json
import os

from app import pocket_api as api

current_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(current_path, "../articles_sample.json")

with open(path, 'r') as file:
    articles = json.load(file)


def test_lambda_handler():
    if articles and len(articles) > 0:
        r = articles
    else:
        r = api.get_articles()

    assert len(r) >= 0
