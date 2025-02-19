from web.extension import db
from web.web_ma import ProductSchema
from web.model import Product
import json
from flask import request
from flask import jsonify

product_schema = ProductSchema(many=False)
products_schema = ProductSchema(many=True)
def add_product_service ():
    name = request.json['name']
    brand = request.json['brand']
    description = request.json['description']
    image = request.json['image']
    price = request.json['price']
    category_id = request.json['category_id']
    
    try:
        print(name)
        new_product = Product(name, brand, description, image,price, category_id)
        print(brand)
        db.session.add(new_product)
        print(new_product)
        print(price)
        print(category_id)
        db.session.commit()
        
        return jsonify({"message": "Product added successfully!", "product": name}), 201
    except Exception as e: 
        db.session.rollback()
        print(e)
        return jsonify({"error": str(e)}), 500
    
def get_product_by_id_service(id):
    product = Product.query.get(id)
    print(product)
    if product:
        return product_schema.jsonify(product)
    else:
        return "Not found product"

def get_all_product_service():
    products = Product.query.all()
    if products:
        return products_schema.jsonify(products)
    else:
        return "Not found product"
    
def update_product_service(id):
    product = Product.query.get(id)
    data = request.json
    if product:
        try: 
            product.name = data.get("name", product.name)
            product.brand = data.get("brand", product.brand)
            product.description = data.get("description", product.description)
            product.image = data.get("image", product.image)
            product.price = data.get("price", product.price)
            product.category_id = data.get("category_id", product.category_id)
            db.session.commit()
            return jsonify({"message": "Product update successfully!", "product": product.name}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        return "Not found product"
    
def delete_product_services(id):
    product = Product.query.get(id)
    if product:
        try:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product delete successfully!", "product": product.name}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500