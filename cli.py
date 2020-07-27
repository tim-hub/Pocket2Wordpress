

from app import pocket_api as api

articles = api.get_articles()

import json

with open('tests/unit/sample.json', 'w') as file:
    file.write(
        json.dumps(articles)
    )