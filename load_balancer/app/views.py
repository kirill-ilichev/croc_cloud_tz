from app import app
from .helpers import get_categories_list, get_meta_data

from .consts import METADATA_API_URI


@app.route("/info", methods=["GET"])
def index():
    categories = get_categories_list(METADATA_API_URI)
    return get_meta_data(categories)


@app.route("/", methods=["GET"])
def abc():
    return "1231223"
