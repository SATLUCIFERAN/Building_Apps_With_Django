
from rest_framework import generics # Import DRF's generic views
from .models import Category, Product # Import the models
from .serializers import CategorySerializer, ProductSerializer # Import the serializers

# CategoryListCreateAPIView: API endpoint to list all categories AND create new ones.
# Inherits from ListCreateAPIView, which provides GET (list) and POST (create) functionality.
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# CategoryRetrieveUpdateDestroyAPIView: API endpoint to retrieve, update, or delete a single category.
# Inherits from RetrieveUpdateDestroyAPIView, which provides GET (retrieve), PUT (update),
# PATCH (partial update), and DELETE functionality.
class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

# ProductListCreateAPIView: API endpoint to list all products AND create new ones.
# Inherits from ListCreateAPIView.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available=True) # Still only show available products for listing
    serializer_class = ProductSerializer

# ProductRetrieveUpdateDestroyAPIView: API endpoint to retrieve, update, or delete a single product.
# Inherits from RetrieveUpdateDestroyAPIView.
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(available=True) # Still only show available products for detail
    serializer_class = ProductSerializer
    lookup_field = 'id'
