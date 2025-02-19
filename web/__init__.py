from flask import Flask
from .product.controller import products
from .category.controller import category
from .user.controller import user
from .extension import db, ma
from .model import Product, User, Category
import os
def create_db(app):
    if not os.path.exists("web/web.db"):
        with app.app_context(): 
            print("created!!")
            db.create_all()
def create_app (config_file = "config.py"):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(category)
    app.register_blueprint(user)
    app.register_blueprint(products)
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    return app