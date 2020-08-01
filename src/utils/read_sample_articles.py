import os
import json


def read_all():
    current_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_path, "../tests/articles_sample.json")

    with open(path, 'r') as file:
        articles = json.load(file)
    return articles
