import json


class Settings:
    def __init__(self):
        with open("settings.json") as f:
            conf = json.load(f)
            self.base_url = conf["base_url"]
            self.load_detect_code_url = conf["load_detect_code_url"]
            self.flight_data_access_url = conf["flight_data_access_url"]
