from .extension import ma

class ProductSchema (ma.Schema):
    class Meta:
        fields = ('id', 'name', 'brand', 'description', 'image', 'price', 'category_id' )
class UserSchema (ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name')
class CategorySchema (ma.Schema):
    class Meta:
        fields = ('id', 'name')    