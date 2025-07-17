# mysite/urls.py

# from django.contrib import admin
# from django.urls import path, include # <--- Add 'include' here!

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')), # <--- Add this line!
#     # Logic & Imagination: path() here is like creating a main entry point in the project's master directory.
#     # 'myfirstapp/' means any URL starting with 'myfirstapp/' will be handled by our app.
#     # include('myapp.urls') tells Django to look inside myapp's urls.py for further patterns.
# ]



############################## Chapter X(10.9) Serving Media Files: #####################################
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings # <--- ADD THIS IMPORT!
# from django.conf.urls.static import static # <--- ADD THIS IMPORT!

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
# ]

# # ONLY add this in development! In production, web servers handle static/media files.
# if settings.DEBUG: # <--- Only serve media files this way when DEBUG is True
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Logic & Imagination: This is a temporary magical conduit, active only during development,
    # that tells Django's development server: "For any request starting with '/media/',
    # go directly to the 'media' storage chamber on the server and fetch the file."



############################## Chapter X(11.6) Django Form ############################################

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views # <--- Ensure 'views' is imported from your app

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name='contact'), # <--- NEW: Contact URL
#     # Logic & Imagination: A new entry in the master directory for the 'contact' page.
#     # This tells the magical router: "When a customer asks for '/contact/',
#     # send them to the 'contact_view' spell in our 'myapp' views."
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



######################### ChapterXII part 2 topic 12.6 User Registration ###############################

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views # Ensure 'views' is imported from your app

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'), # <--- NEW: Registration URL
#     # Logic & Imagination: A new entry in the master directory: "When a traveler
#     # seeks '/register/', guide them to the 'register' initiation ritual."
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





######################### ChapterXII part 2 topic 12.7 User Registration Login ###############################

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myfirstapp/', include('myapp.urls')),
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'), # <--- NEW: Login URL
#     # Logic & Imagination: Another entry in the master directory: "When a customer
#     # seeks '/login/', guide them to the 'user_login' ritual."
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




########################## Chapter XII Part 2 topic 12.8 Update for user logout ###################################


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
#     path('logout/', views.user_logout, name='logout'), # <--- NEW: Logout URL
#     # Logic & Imagination: Another entry in the master directory: "When a customer
#     # seeks '/logout/', guide them to the 'user_logout' ritual."
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




########################## Chapter XII Part 3 Add Home Page  ###################################


# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views # Ensure 'views' is imported from your app

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home_view, name='home'), # <--- NEW: Home Page URL (MUST BE FIRST FOR ROOT)
#     # Logic & Imagination: This is the master entry point. When a traveler
#     # arrives at the base address of your realm, they are guided to the 'home_view'.
#     path('myfirstapp/', include('myapp.urls')), # Keep this for product list, etc.
#     path('contact/', views.contact_view, name='contact'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





########################## Chapter XII Part 3 Profile Page  ###################################


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
#     path('profile/', views.profile_view, name='profile'), # <--- NEW: Profile URL
#     # Logic & Imagination: A new entry for the customer's personal vault.
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



########################## Chapter XII Part4 LoginRequiredMixin  ###################################

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
#     path('profile/', views.profile_view, name='profile'),
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # <--- NEW: Order History URL
#     # Logic & Imagination: An entry for the customer's order ledger.
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



############################ ChapterXII(Part4) Topic12.12 Access to Staff/Superusers    #################################

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
#     path('profile/', views.profile_view, name='profile'),
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'),
#     path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'), # <--- NEW: Vendor Dashboard URL
#     # Logic & Imagination: An entry for the Vendor Guild Hall.
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



######################### Chapter XII Part 6 topic 12.18  Crafting the Profile Editing Forms: ###########################

# mysite/urls.py (updated for Profile Update URL)

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
#     path('profile/', views.profile_view, name='profile'),
#     path('profile/edit/', views.profile_update_view, name='profile_edit'), 
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'),
#     path('vendor-dashboard/', views.vendor_dashboard_view, name='vendor_dashboard'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



############################## ChapterXIV topic 14.1 Implementing Basic Product Search ##############################

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
#     # The 'profile_view' function was refactored to 'UserProfileView' class.
#     # The 'profile_update_view' function was refactored to 'UserProfileUpdateView' class.
#     # The 'vendor_dashboard_view' function was refactored to 'VendorDashboardView' class.
#     # Note: 'OrderHistoryView' was already correctly using .as_view()
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), # <--- CRITICAL FIX: Use .as_view() and consistent name
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), # <--- CRITICAL FIX: Use .as_view() and consistent name
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # This was already correct!
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'), # <--- CRITICAL FIX: Use .as_view()
#     # --- END CRITICAL MODIFICATION ---
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





################################ ChapterXIV topic 15.2  Adding Products to the Cart #####################################

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



######################### ChapterXIV topic 15.3 The Satchel's Glimpse: Displaying Cart Contents ######################

# mysite/urls.py (updated with cart_detail URL)

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
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # RETAINED from 15.2    
#     path('cart/', views.cart_detail, name='cart_detail'),     
# ]

# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



######################### ChapterXIV topic 15.4 The Satchel's Refinement: Modifying Cart Contents ######################


# mysite/urls.py (updated with cart modification URLs)

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls), # RETAINED
#     path('', views.home_view, name='home'), # RETAINED
#     path('myfirstapp/', include('myapp.urls')), # RETAINED
#     path('contact/', views.contact_view, name='contact'), # RETAINED
#     path('register/', views.register, name='register'), # RETAINED
#     path('login/', views.user_login, name='login'), # RETAINED
#     path('logout/', views.user_logout, name='logout'), # RETAINED
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), # RETAINED
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), # RETAINED
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # RETAINED
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'), # RETAINED

#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # RETAINED from 15.2
#     path('cart/', views.cart_detail, name='cart_detail'), # RETAINED from 15.3

#     # --- NEW: Cart Modification URLs ---
#     path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), # NEW URL for updating cart item quantity
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # NEW URL for removing cart item
#     # --- END NEW ---
# ]

# if settings.DEBUG: # RETAINED
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # RETAINED



######################### ChapterXIV topic 15.5: The Final Incantation: Implementing Checkout ######################

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls), # RETAINED
#     path('', views.home_view, name='home'), # RETAINED
#     path('myfirstapp/', include('myapp.urls')), # RETAINED
#     path('contact/', views.contact_view, name='contact'), # RETAINED
#     path('register/', views.register, name='register'), # RETAINED
#     path('login/', views.user_login, name='login'), # RETAINED
#     path('logout/', views.user_logout, name='logout'), # RETAINED
#     path('profile/', views.UserProfileView.as_view(), name='profile_view'), # RETAINED
#     path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), # RETAINED
#     path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # RETAINED
#     path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'), # RETAINED

#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # RETAINED from 15.2
#     path('cart/', views.cart_detail, name='cart_detail'), # RETAINED from 15.3
#     path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), # RETAINED from 15.4
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # RETAINED from 15.4

#     # --- NEW: Checkout and Order Confirmation URLs ---
#     path('checkout/', views.checkout, name='checkout'), # NEW URL for the checkout page
#     path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'), # NEW URL for order confirmation
#     # --- END NEW ---
# ]

# if settings.DEBUG: # RETAINED
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # RETAINED




######################### ChapterXVI topic16.4 : Defining the Conduit Paths: Setting Up API URLs ######################

# mysite/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views # RETAINED

urlpatterns = [
    path('admin/', admin.site.urls), # RETAINED
    path('', views.home_view, name='home'), # RETAINED
    path('myfirstapp/', include('myapp.urls')), # RETAINED
    path('contact/', views.contact_view, name='contact'), # RETAINED
    path('register/', views.register, name='register'), # RETAINED
    path('login/', views.user_login, name='login'), # RETAINED
    path('logout/', views.user_logout, name='logout'), # RETAINED
    path('profile/', views.UserProfileView.as_view(), name='profile_view'), # RETAINED
    path('profile/edit/', views.UserProfileUpdateView.as_view(), name='profile_update'), # RETAINED
    path('orders/', views.OrderHistoryView.as_view(), name='order_history'), # RETAINED
    path('vendor-dashboard/', views.VendorDashboardView.as_view(), name='vendor_dashboard'), # RETAINED

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), # RETAINED from 15.2
    path('cart/', views.cart_detail, name='cart_detail'), # RETAINED from 15.3
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'), # RETAINED from 15.4
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'), # RETAINED from 15.4

    path('checkout/', views.checkout, name='checkout'), # RETAINED from 15.5
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'), # RETAINED from 15.5

    # --- NEW: Include API URLs ---
    path('api/', include('myapp.api_urls')), # NEW: Include API URLs under the /api/ path
    # --- END NEW ---     
]

if settings.DEBUG: # RETAINED
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # RETAINED