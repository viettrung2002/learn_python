from flask import Blueprint
from .services import add_user_service, login_services
user = Blueprint ("user", __name__)

@user.route("/user/add", methods = ['POST'])
def add_user():
    return add_user_service()

@user.route("/login", methods = ['POST'])
def login():
    return login_services()