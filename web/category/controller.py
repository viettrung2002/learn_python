from flask import Blueprint
from .services import add_category_service
category = Blueprint ("category", __name__)

@category.route("/product-management/category", methods = ['POST'])
def add_category():
    return add_category_service()