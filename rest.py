import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


def login(username, password):
    response = requests.post(url=config["rest_login_url"],
                             data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json()["token"]


def get_posts(token, params):
    response = requests.get(url=config["rest_posts_url"], headers={"X-Auth-Token": token}, params=params)
    if response.status_code == 200:
        return response.json().get("data")


def publish_post(token, post_data):
    response = requests.post(url=config["rest_posts_url"], headers={"X-Auth-Token": token}, data=post_data)
    if response.status_code == 200:
        return response.json()['id']
