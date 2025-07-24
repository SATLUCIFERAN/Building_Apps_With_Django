
############ Chapter VII Part 3 topics 7.9 The URL: The Magical Address Book #############

# from django.urls import path
# from . import views 

# urlpatterns = [
#     path("", views.index, name="index"),    
    
# ]


########## Chapter X PART 2  topics 10.7.1 ListView: Displaying a Catalog of Scrolls #################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),
# ]



########## Chapter X PART 2  topics 10.7.2 DetailView: Revealing a Single Scroll's Secrets #################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),
#     path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
# ]



################ Chapter XIII topic 13.1 The Product's Portrait: Adding ImageField to the Product Model ################

# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),
#     path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name="product_detail"),
    
# ]



##################### Chapter XVIII topic 18.3: The Client-Side Charm: Conjuring Payment Elements ################# 


# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),    
#     path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),  
#     path('checkout_view/', views.checkout_view, name='checkout_view'),   # <----- New url    
# ]



################### Chapter XVIII 18.4: The Server-Side Ledger: Processing Charges with Django ##############

# from django.urls import path
# from . import views


# urlpatterns = [
#     path("", views.ProductListView.as_view(), name="product_list"),    
#     path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),
#     path('checkout_view/', views.checkout_view, name='checkout_view'),     
#     path('stripe-checkout/', views.stripe_payment_form_view, name='stripe_checkout_form'), # <----- New url  
#     path('process-payment/', views.process_payment, name='process_payment'),  # <----- New url     
# ]


################## Chapter XVIII 18.5:The Unified Checkout: Integrating Payment into checkout.html ##############


from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),    
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(),name="product_detail"),
    # path('checkout_view/', views.checkout_view, name='checkout_view'),     
    # path('stripe-checkout/', views.stripe_payment_form_view, name='stripe_checkout_form'), 
    path('process-payment/', views.process_payment, name='process_payment'),     
]
