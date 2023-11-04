import pytest
from rest import get_posts, publish_post


class TestREST:
    def test_get_posts(self, rest_login, rest_title):
        posts = get_posts(rest_login, {"owner": "notMe"})
        assert rest_title in [item['title'] for item in posts]

    def test_publish_post(self, rest_login, post_data):
        post_id = publish_post(rest_login,
                               {"title": post_data[0], "description": post_data[1],
                                "content": post_data[2]})
        posts = get_posts(rest_login, {"owner": "me", "description": post_data[1]})
        assert post_id in [item['id'] for item in posts]


if __name__ == '__main__':
    pytest.main(["-v"])
