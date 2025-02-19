from web.extension import db
from web.model import User
import json
from flask import request
from web.web_ma import UserSchema
from flask import jsonify
user_schema = UserSchema(many=False)
def add_user_service():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    role = 'user'
    existing_user = User.query.filter(User.username == username, User.password == password).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400
    try:
        new_user = User(username, password, name, role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "User added successfully!",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "name": new_user.name,
            }
        }), 201 
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
def login_services():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter(User.username == username, User.password == password).first()
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401
    
    return user_schema.jsonify(user) 