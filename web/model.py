from web.extension import db
import enum

class RoleEnum(enum.Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    role = db.Column(db.Enum(RoleEnum))
    def __init__(self, username, password, name, role):
        self.username = username
        self.password = password
        self.name = name
        self.role = role
        

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    image = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    def __init__(self, name, brand, description, image, price, category_id):
        self.name = name
        self.brand = brand
        self.description = description
        self.image = image
        self.price = price
        self.category_id = category_id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

        
