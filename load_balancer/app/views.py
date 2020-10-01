import math
import time

from app import app

from .consts import METADATA_API_URI
from .helpers import get_categories_list, get_meta_data


@app.route("/info", methods=["GET"])
def info():
    """Method to get MetaData info"""
    categories = get_categories_list(METADATA_API_URI)
    return get_meta_data(categories)


@app.route("/load", methods=["GET"])
def load():
    """Method to initiates fake CPU stress"""
    start_time = time.clock()
    while time.clock() - start_time < 40:
        math.factorial(100)
    return "Нагрузка успешно создана"
