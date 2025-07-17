
from rest_framework import serializers
from .models import Category, Product # Import the models we want to serialize

# CategorySerializer: Translates Category model instances into API-consumable formats.
# This serializer will expose the 'id', 'name', and 'slug' fields of a Category.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category # Specify the Django model this serializer is for
        fields = ['id', 'name', 'slug'] # List the fields from the model to be included in the API output
        # You could also use fields = '__all__' to include all fields,
        # but it's often better practice to explicitly list them for clarity and control.

# ProductSerializer: Translates Product model instances into API-consumable formats.
# This serializer will expose various fields of a Product, including its category.
class ProductSerializer(serializers.ModelSerializer):
    # For ForeignKey relationships, by default, DRF will just show the primary key (ID).
    # To show the full category name or details, we can nest the CategorySerializer.
    # Here, we'll just show the category's name for simplicity in the product listing.
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product # Specify the Django model this serializer is for
        fields = [
            'id', 'name', 'slug', 'category', 'category_name', # 'category' will be the ID, 'category_name' will be the name
            'image', 'description', 'price', 'available', 'created', 'updated'
        ]
        # 'read_only_fields' can be used for fields that should not be set via the API,
        # but are generated automatically (like 'created', 'updated').
        read_only_fields = ['created', 'updated']