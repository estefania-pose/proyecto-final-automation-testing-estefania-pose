import pytest

@pytest.fixture(scope="module")
def base_url_posts():
    return "https://jsonplaceholder.typicode.com/posts"