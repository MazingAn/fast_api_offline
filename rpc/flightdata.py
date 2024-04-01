import requests
import pandas as pd
from config.settings import Settings

settings = Settings()


def load_flight_data(id, params):
    """
    Load the params
    """
    data = {}
    for param in params:
        url = "{}{}{}/{}".format(
            settings.base_url, settings.flight_data_access_url, id, param
        )
        response = requests.get(url)
        if response.status_code == 200:
            print(param)
            data[param] = response.json()
    return pd.DataFrame(data)
