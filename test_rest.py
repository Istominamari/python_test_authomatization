import pytest
from rest import get_posts, publish_post

class TestREST:
    def test_getPosts(self, rest_login, rest_title):
        posts = get_posts(rest_login, {"owner":"notMe"})
        assert rest_title in [item['title'] for item in posts]

    def test_publishPost(self, rest_login, rest_post_data):
        id = publish_post(rest_login,
                        {"title": rest_post_data[0], "description": rest_post_data[1], "content": rest_post_data[2]})
        posts = get_posts(rest_login, {"owner":"me", "description": rest_post_data[1]})
        assert id in [item['id'] for item in posts]


if __name__ == '__main__':
    pytest.main(["-v"])