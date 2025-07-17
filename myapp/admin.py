

# from django.contrib import admin
# from .models import Category, Product # <--- Import your models here!

# # Register your models here.

# admin.site.register(Category) # <--- Register the Category model
# # Logic & Imagination: You're telling the ledger, "Include the 'Category' data scrolls!"

# admin.site.register(Product) # <--- Register the Product model
# # Logic & Imagination: You're telling the ledger, "Include the 'Product' data scrolls too!"


##############################################################################################



# from django.contrib import admin
# from .models import Category, Product

# # Register your models here.

# @admin.register(Category) # <--- Use the decorator to register the model
# class CategoryAdmin(admin.ModelAdmin):
#     """
#     Customizes the display and behavior of the Category model in the Django Admin.
#     """
#     list_display = ['name', 'slug'] # Logic & Imagination: Show 'name' and 'slug' in the category list.
#     prepopulated_fields = {'slug': ('name',)} # Logic & Imagination: Automatically fill 'slug' from 'name'.

# @admin.register(Product) # <--- Use the decorator to register the model
# class ProductAdmin(admin.ModelAdmin):
#     """
#     Customizes the display and behavior of the Product model in the Django Admin.
#     """
#     list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
#     # Logic & Imagination: Display these specific fields in the product list view.

#     list_filter = ['available', 'created', 'updated', 'category']
#     # Logic & Imagination: Add magical filters for these fields on the sidebar.

#     list_editable = ['price', 'available']
#     # Logic & Imagination: Allow direct editing of 'price' and 'available' from the list.

#     prepopulated_fields = {'slug': ('name',)}
#     # Logic & Imagination: Automatically fill 'slug' from 'name' when creating/editing.

#     raw_id_fields = ['category']
#     # Logic & Imagination: For 'category', show a search icon instead of a dropdown
#     # for large numbers of categories, making selection faster.

#     search_fields = ['name', 'description', 'slug']
#     # Logic & Imagination: Add a magical search bar to find products by name, description, or slug.
 



################################  Chapter XII Part 5 topic12.15 Register UserProfile  ##################################################


# from django.contrib import admin
# from .models import Category, Product, UserProfile # <--- NEW: Import UserProfile

# # Register your models here.
# admin.site.register(UserProfile) # <--- NEW: Register UserProfile
# # Detailed Explanation: This line tells Django's administration site to create an interface
# # for managing UserProfile objects. Once registered, your superuser can perform CRUD
# # (Create, Read, Update, Delete) operations on UserProfile instances directly through the web browser.
# # Logic & Imagination: You are adding the 'UserProfile' scrolls to the visible
# # sections of the Grand Control Chamber's archives, so you, the Master Alchemist,
# # can inspect and manage them directly, just like your Products and Categories.


# @admin.register(Category) 
# class CategoryAdmin(admin.ModelAdmin):

#     list_display = ['name', 'slug'] 
#     prepopulated_fields = {'slug': ('name',)} 


# @admin.register(Product) 
# class ProductAdmin(admin.ModelAdmin):
    
#     list_display = ['name', 'slug', 'price', 'available', 'created', 'updated'] 
#     list_filter = ['available', 'created', 'updated', 'category']    
#     list_editable = ['price', 'available']    
#     prepopulated_fields = {'slug': ('name',)}   
#     raw_id_fields = ['category']   
#     search_fields = ['name', 'description', 'slug']


    
 
 ################################  Chapter XIII  topic13.3 Managing Product Images in Django Admin  ###################################

from django.contrib import admin
from .models import Category, Product, UserProfile

# Register your models here.
admin.site.register(UserProfile)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'image'] # <--- NEW/MODIFIED: Add 'image' to list_display
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available', 'image'] # <--- NEW/MODIFIED: Add 'image' to list_editable (optional, but convenient)
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['category']
    search_fields = ['name', 'description', 'slug']