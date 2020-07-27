from utils.read_sample_articles import read_all
from worker.formatter import format_all

def test_fomat_all():
    articles = read_all()

    r = format_all(articles.items())

    print(r)