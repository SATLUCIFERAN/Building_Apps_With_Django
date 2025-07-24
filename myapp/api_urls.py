
############################## Chapter XVI topic 16.1 Step-by-Step: Installing and Configuring DRF ########################


from django.urls import path
from . import api_views 

app_name = 'api'

urlpatterns = [
    # API endpoint for listing AND CREATING categories
    path('categories/', api_views.CategoryListCreateAPIView.as_view(), name='category-list'),

    # API endpoint for retrieving, UPDATING, AND DELETING a single category
    path('categories/<slug:slug>/', api_views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # API endpoint for listing AND CREATING products
    path('products/', api_views.ProductListCreateAPIView.as_view(), name='product-list'),

    # API endpoint for retrieving, UPDATING, AND DELETING a single product
    path('products/<int:id>/', api_views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
