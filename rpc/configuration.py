import requests
from config.settings import Settings

settings = Settings()


def load_detect_code(action_name):
    url = settings.base_url + settings.load_detect_code_url + action_name
    url = "{}{}{}".format(settings.base_url, settings.load_detect_code_url, action_name)
    print(url)
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        ret = response.json()
        return ret
    return None
