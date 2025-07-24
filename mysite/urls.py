

##################### Chapter VII Part 3 topics 7.9 The URL: The Magical Address Book #################

# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls'))
# ]



################## Chapter X  PART 2 topic 10.9 Serving Media Files: Displaying Your Dynamic Assets ##############

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




################## Chapter XI  topic 11.6 Django Forms: The Alchemist's Form-Building Spells ##############

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views # <--- Ensure 'views' is imported from your app

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




################# Chapter XII part 2 12.6 User Registration: Initiating a New Identity ############## 

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





##################### Chapter XII part 2 12.7 User Login: Presenting the Access Amulet ##############

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



##################### Chapter XII part 2 12.8 User Logout: Relinquishing the Amulet ############## 

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout')
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



##################### Chapter XII  Part 3: The Alchemist's Welcome: Crafting the Home Page (/) ##############  {% endcomment %}


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout')
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


######### Chapter XII  Part 4 topic 12.10 Protecting Views with @login_required: The Basic Ward ###########

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/',views.profile_view, name='profile'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


############# ChapterXII  Part4  topic 12.11 Protecting Class-Based Views with LoginRequiredMixin:################## 



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/', views.profile_view, name='profile'),    
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # <--- NEW: Order History URL
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




############################ ChapterXII  Part4  topic 12.12 Restricting Access to Staff/Superusers: Elite Wards  #############################



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/', views.profile_view, name='profile'),    
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





################### Chapter XII topics12.18 Crafting the Profile Editing Forms: The Customer's Quill ################ 


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/', views.profile_view, name='profile'),  
#     path('profile/edit',views.profile_update_view, name='profile_edit'),  
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



################## (Ensure) Chapter XII Part 6 topics12.18 Crafting the Profile Editing Forms: The Customer's Quill ################ 


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views 

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name= 'contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('profile/', views.profile_view, name='profile'),  
#     path('profile/edit',views.profile_update_view, name='profile_edit'),  
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



############ Chapter XIV  Anomaly 3: The Misaligned Portals-Correcting mysite/urls.py


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')), 
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),

#     # --- CRITICAL MODIFICATION: Updated to reference Class-Based Views using .as_view() ---    
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), # <--- CRITICAL FIX: Use .as_view() and consistent name
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), # <--- CRITICAL FIX: Use .as_view() and consistent name
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # This was already correct!
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'), # <--- CRITICAL FIX: Use .as_view()
#     # --- END CRITICAL MODIFICATION ---
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





######################### ChapterXIV topic 15.2  The Gathering Spell: Adding Products to the Cart ######################


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')), 
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),   
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), 
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), 
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
    
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



################## ChapterXV topic15.3 The Satchel's Glimpse: Displaying Cart Contents #############



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')), 
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),   
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), 
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), 
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
#     path('cart/',views.cart_detail, name='cart_details'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



################### Chapter XV topic 15.4  Step-by-Step: Forging the Satchel's Refinement ####################



# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')), 
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),   
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), 
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), 
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
#     path('cart/',views.cart_detail, name='cart_details'),

#     # --- NEW: Cart Modification URLs ---
#     path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), # NEW URL for updating cart item quantity
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # NEW URL for removing cart item
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




######################################### Chapter XV topic 15.5: The Final Incantation: Implementing Checkout############################ 


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'),
#     path('myfirstapp/', include('myapp.urls')), 
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),   
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), 
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), 
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
#     path('cart/',views.cart_detail, name='cart_details'),    
#     path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), 
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

#     # --- NEW: Checkout and Order Confirmation URLs ---
#     path('checkout/', views.checkout, name='checkout'), # NEW URL for the checkout page
#     path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'), # NEW URL for order confirmation

#  ] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



############################## Chapter XVI topic 16.1 Step-by-Step: Installing and Configuring DRF ########################


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('myfirstapp/', include('myapp.urls')), 
    path('contact/', views.contact_view, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),   
    path('profile/', views.UserProfileView.as_view(), name='profile_view'), 
    path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), 
    path('orders/', views.OrderHistoryView.as_view(), name='order_history'), 
    path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  
    path('cart/',views.cart_detail, name='cart_details'),    
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), 
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),    
    path('checkout/', views.checkout, name='checkout'), 
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'), 
    path('api/', include('myapp.api_urls')), # NEW URL

 ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

