from web.extension import db
from web.model import Category
from flask import jsonify
import json
from flask import request

def add_category_service():
    name =  request.json['name']
    try:
        new_category = Category(name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify({"message": "Category added successfully!", "category": name}), 201
    except Exception as e: 
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

