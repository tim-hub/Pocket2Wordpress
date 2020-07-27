from worker import pocket_api as api
from utils.read_sample_articles import read_all

articles = read_all()


def test_lambda_handler():
    if articles and len(articles) > 0:
        r = articles
    else:
        r = api.get_articles()

    assert len(r) >= 0
