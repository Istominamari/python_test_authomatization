import requests
import yaml
import logging

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


def login(username, password):
    logging.debug(f"Login user \"{username}\".")
    try:
        response = requests.post(url=config["rest_login_url"],
                                 data={"username": username, "password": password})
    except:
        logging.exception("Exception while login.")
        return None
    if response.status_code == 200:
        return response.json()["token"]
    else:
        logging.error(f"Login failed with code \"{response.status_code}\".")
        return None


def get_posts(token, params):
    logging.debug(f"Get posts with params: \"{params}\".")
    try:
        response = requests.get(url=config["rest_posts_url"], headers={"X-Auth-Token": token}, params=params)
    except:
        logging.exception(f"Exception while getting posts.")
        return []
    if response.status_code == 200:
        return response.json().get("data")
    else:
        logging.error(f"Getting posts failed with code \"{response.status_code}\".")
        return []


def publish_post(token, post_data):
    logging.debug(f"Publish post with data: \"{post_data}\".")
    try:
        response = requests.post(url=config["rest_posts_url"], headers={"X-Auth-Token": token}, data=post_data)
    except:
        logging.exception(f"Exception while publish post.")
        return None
    if response.status_code == 200:
        return response.json()['id']
    else:
        logging.error(f"Publish post failed with code \"{response.status_code}\".")
        return None


if __name__ == '__main__':
    print(login('azaza', 'ololo'))
