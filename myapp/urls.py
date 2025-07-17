
# from django.urls import path
# from . import views 

# urlpatterns = [
#     path("", views.index, name="index"),
    
    
# ]



########### ChapterX(10.7.1) ListView: Displaying a Catalog of Scrolls  ###########

# myapp/urls.py (updated for ProductListView)

# from django.urls import path
# from . import views

# urlpatterns = [
#     # path("", views.index, name="index"), # You can comment out or remove this old line
#     path("", views.ProductListView.as_view(), name="product_list"), # <--- NEW: Map to our CBV
#     # Logic & Imagination: We're updating our app's address book.
#     # Now, the root path "" will call our ProductListView.
#     # .as_view() is a magical method that turns the class into a callable view function.
# ]




#################### ChapterX(10.7.2) DetailView ####################

# myapp/urls.py (updated for ProductDetailView)

from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    # <slug:slug> captures the slug from the URL
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"), # <--- NEW: Map to DetailView
    # Logic & Imagination: We're adding a new entry to our address book:
    # "Any path that looks like '/some-product-slug/' should call our ProductDetailView.
    # The '<slug:slug>' part is a magical placeholder that captures the slug from the URL."
]





#################### Chapter XIII tipics13.1 Adding ImageField to the Product Model ####################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),
#     # <slug:slug> captures the slug from the URL
#    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"), # <--- NEW: Map to DetailView
#     # Logic & Imagination: We're adding a new entry to our address book:
#     # "Any path that looks like '/some-product-slug/' should call our ProductDetailView.
#     # The '<slug:slug>' part is a magical placeholder that captures the slug from the URL."
# ]



######################### ChapterXVIII Section 18.3: The Client-Side Charm: Conjuring Payment Elements ######################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),    
#     path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),  
#     path('checkout_view/', views.checkout_view, name='checkout_view'),      
# ]


######################### ChapterXVIII Section Section 18.4: The Server-Side Ledger: Processing Charges with Django #################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),    
#     path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),     
#     path('stripe-checkout/', views.stripe_payment_form_view, name='stripe_checkout_form'), 
#     path('process-payment/', views.process_payment, name='process_payment'),     
# ]


##################################### ChapterXVIII Section 18.5: The Unified Checkout ###############################


from django.urls import path
from . import views



urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),    
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),   
    path('process-payment/', views.process_payment, name='process_payment'),     
]
    

