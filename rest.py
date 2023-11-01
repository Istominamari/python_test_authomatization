import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def login():
    response = requests.post(url=data["rest_login_url"], data={"username": data["rest_username"], "password": data["rest_password"]})
    if response.status_code == 200:
        return response.json()["token"]

def get_posts(token, params):
    response = requests.get(url=data["rest_posts_url"], headers={"X-Auth-Token": token}, params=params)
    if response.status_code == 200:
        return response.json().get("data")

def publish_post(token, post_data):
    response = requests.post(url=data["rest_posts_url"], headers={"X-Auth-Token": token}, data=post_data)
    if response.status_code == 200:
        return response.json()['id']

if __name__ == "__main__":
    token = login()
    print(get_posts(token, {"owner":"notMe", "title":"White cat"}))