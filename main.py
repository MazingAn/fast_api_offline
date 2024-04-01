from fastapi import FastAPI
from config.settings import Settings
from service import detect_service as ds

settings = Settings()
app = FastAPI()


@app.get("/detect_code/{action_name}")
def load_detect_code(action_name: str):
    if action_name == "起飞":
        return """
def setparams():
    \treturn "指示空速 过载".split()

def detect(data):
    \treturn data.values.tolist()
"""


@app.get("/params/{id}/{param}")
def load_param_by_id(id: int, param: str):
    return [0, 2, 3, 4, 5, 6, 1, 2, 3, 1, 1, 1, 2, 1, 2, 12, 4, 1, 21, 4, 12]


@app.get("/detect/{id}/{action_name}")
def detect_test(id: int, action_name: str):
    return ds.run(id, action_name)
