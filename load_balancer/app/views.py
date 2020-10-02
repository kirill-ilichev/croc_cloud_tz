import math
import time

import requests
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
    try:
        public_ip = requests.get(METADATA_API_URI+"public-ipv4")
        public_ip_text = "Публичный IP ноды - {0}".format(public_ip)
    except requests.exceptions.ConnectionError:
        public_ip_text = "Не удалось получить публичный IP ноды"
    start_time = time.clock()
    while time.clock() - start_time < 40:
        math.factorial(99999)
    return "Нагрузка успешно создана. {0}".format(public_ip_text)
