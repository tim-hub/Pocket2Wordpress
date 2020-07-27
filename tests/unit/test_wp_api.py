from worker import wordpress_api as api


def test_fetch():
    r = api.fetch_posts()
    assert len(r) >= 0
