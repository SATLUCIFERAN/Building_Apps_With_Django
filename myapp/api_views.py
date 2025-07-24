
############################## Chapter XVI topic 16.1 Step-by-Step: Installing and Configuring DRF ########################


from rest_framework import generics 
from .models import Category, Product 
from .serializers import CategorySerializer, ProductSerializer 

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available=True) 
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(available=True) 
    serializer_class = ProductSerializer
    lookup_field = 'id'
