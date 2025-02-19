from flask import Blueprint
from .services import add_product_service, get_product_by_id_service, update_product_service, get_all_product_service, delete_product_services
products = Blueprint ("products", __name__)

@products.route("/product-management/product", methods = ['POST'])
def add_product():
    return add_product_service()

@products.route("/product/<int:id>", methods = ["GET"])
def get_product_by_id(id):
    return get_product_by_id_service(id)

@products.route("/products", methods = ["GET"])
def get_all_product():
    return get_all_product_service()

@products.route("/product/update/<int:id>", methods = ["POST"])
def update_product(id):
    return update_product_service(id)

@products.route("/product/delete/<int:id>", methods = ["DELETE"])
def delete_product(id):
    return delete_product_services(id)