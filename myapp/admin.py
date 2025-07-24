

##################### Chapter IX  PART 1 topics 9.3 Registering Your Models: Revealing Your Data Scrolls in the Ledger ########

# from django.contrib import admin
# from .models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)


##################### Chapter IX  PART 2 topics 9.4 Customizing Model Display: Making Your Scrolls Readable ########

# from django.contrib import admin
# from .models import Category, Product

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display        = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display        = ['name', 'slug', 'price', 'available', 'created', 'updated']
#     list_filter         = ['available', 'created', 'updated', 'category']
#     list_editable       = ['price', 'available']
#     prepopulated_fields = {'slug': ('name',)}
#     raw_id_fields       = ['category']
#     search_fields       = ['name', 'description', 'slug']



################# Chapter XII Part5  topics 12.15  Implementing the Profile Model: Forging Personalized Scrolls ##############

# from django.contrib import admin
# from .models import Category, Product , UserProfile


# # Register your models here.
# admin.site.register(UserProfile)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display        = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display        = ['name', 'slug', 'price', 'available', 'created', 'updated']
#     list_filter         = ['available', 'created', 'updated', 'category']
#     list_editable       = ['price', 'available']
#     prepopulated_fields = {'slug': ('name',)}
#     raw_id_fields       = ['category']
#     search_fields       = ['name', 'description', 'slug']






################ Chapter XIII topic 13.1 The Product's Portrait: Adding ImageField to the Product Model ################


from django.contrib import admin
from .models import Category, Product , UserProfile


# Register your models here.
admin.site.register(UserProfile)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display        = ['name', 'slug', 'price', 'available', 'created', 'updated','image']
    list_filter         = ['available', 'created', 'updated', 'category']
    list_editable       = ['price', 'available','image']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields       = ['category']
    search_fields       = ['name', 'description', 'slug']

