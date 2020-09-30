import math
import time

from app import app

from .consts import METADATA_API_URI
from .helpers import get_categories_list, get_meta_data


@app.route("/info", methods=["GET"])
def index():
    categories = get_categories_list(METADATA_API_URI)
    return get_meta_data(categories)


@app.route("/load", methods=["GET"])
def load():
    start_time = time.clock()
    while time.clock() - start_time < 20:
        math.factorial(100)
    return "Нагрузило, проверяй"
