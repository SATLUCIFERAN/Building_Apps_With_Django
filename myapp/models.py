
################# Chapter VIII Part 2 topics 8.5 Defining Your First Models: Category and Product ##############

# from django.db import models
# from django.db.models import Index

# class Category(models.Model):

#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name



# class Product(models.Model):

#     category = models.ForeignKey(
#         Category,
#         related_name='products',
#         on_delete=models.CASCADE
#     )

#     name        = models.CharField(max_length=200, db_index=True)
#     slug        = models.SlugField(max_length=200, db_index=True, unique=True)
#     image       = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     description = models.TextField(blank=True)
#     price       = models.DecimalField(max_digits=10, decimal_places=2)
#     available   = models.BooleanField(default=True)
#     created     = models.DateTimeField(auto_now_add=True)
#     updated     = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         indexes = [
#             models.Index(fields=['id', 'slug']),
#         ]

#     def __str__(self):
#         return self.name



################# Chapter XII Part5  topics 12.15  Implementing the Profile Model: Forging Personalized Scrolls ##############



# from django.db import models
# from django.contrib.auth.models import User # <--- NEW: Import Django's built-in User model
# from PIL import Image # <--- NEW: Import Image for image processing (install Pillow if not already)


# class Category(models.Model):
    
#     name = models.CharField(max_length=200, db_index=True)   
#     slug = models.SlugField(max_length=200, unique=True)    

#     class Meta:
#         ordering = ('name',) 
#         verbose_name = 'category' 
#         verbose_name_plural = 'categories' 

#     def __str__(self):
        
#         return self.name       


# class Product(models.Model):
   
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
   
#     name = models.CharField(max_length=200, db_index=True)  
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)  
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)   
#     description = models.TextField(blank=True)  
#     price = models.DecimalField(max_digits=10, decimal_places=2)  
#     available = models.BooleanField(default=True)  
#     created = models.DateTimeField(auto_now_add=True)   #
#     updated = models.DateTimeField(auto_now=True)
   
#     class Meta:
#         ordering = ('name',) 
#         indexes = [
#             models.Index(fields=['id', 'slug']), 
#         ]

#     def __str__(self):
#         return self.name
        

# # # ... (Product and Category models as before) ...

# class UserProfile(models.Model):
#     """
#     Extends the Django User model with additional profile information.
#     This model holds custom data for each user, linked via a OneToOneField.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # <--- The One-to-One link   
#     phone_number = models.CharField(max_length=20, blank=True, null=True)   
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)   
#     country = models.CharField(max_length=100, blank=True, null=True)   
#     profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)
   

#     def __str__(self):   
             
#         return f'{self.user.username} Profile'
    
#     def save(self, *args, **kwargs):
        
#         super().save(*args, **kwargs)      
#         if self.profile_picture:             
#             img = Image.open(self.profile_picture.path)          
#             if img.height > 300 or img.width > 300:
#                output_size = (300, 300)                 
#                img.thumbnail(output_size)               
#                img.save(self.profile_picture.path) 





################ Chapter XIII topic 13.1 The Product's Portrait: Adding ImageField to the Product Model ################



# from django.db import models
# from django.contrib.auth.models import User # <--- NEW: Import Django's built-in User model
# from PIL import Image # <--- NEW: Import Image for image processing (install Pillow if not already)
# from django.urls import reverse


# class Category(models.Model):
    
#     name = models.CharField(max_length=200, db_index=True)   
#     slug = models.SlugField(max_length=200, unique=True)    

#     class Meta:
#         ordering = ('name',) 
#         verbose_name = 'category' 
#         verbose_name_plural = 'categories' 

#     def __str__(self):
        
#         return self.name       


# class Product(models.Model):
   
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
   
#     name = models.CharField(max_length=200, db_index=True)  
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)  
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null = True)   
#     description = models.TextField(blank=True)  
#     price = models.DecimalField(max_digits=10, decimal_places=2)  
#     available = models.BooleanField(default=True)  
#     created = models.DateTimeField(auto_now_add=True)   #
#     updated = models.DateTimeField(auto_now=True)
   
#     class Meta:
#         ordering = ('name',) 
#         indexes = [
#             models.Index(fields=['id', 'slug']), 
#         ]

#     def __str__(self):
#         return self.name
    

#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse("product_detail", args=[self.id , self.slug])
    
       

# class UserProfile(models.Model):
#     """
#     Extends the Django User model with additional profile information.
#     This model holds custom data for each user, linked via a OneToOneField.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # <--- The One-to-One link   
#     phone_number = models.CharField(max_length=20, blank=True, null=True)   
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)   
#     country = models.CharField(max_length=100, blank=True, null=True)   
#     profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)
   

#     def __str__(self):   
             
#         return f'{self.user.username} Profile'
    
#     def save(self, *args, **kwargs):
        
#         super().save(*args, **kwargs)      
#         if self.profile_picture:             
#             img = Image.open(self.profile_picture.path)          
#             if img.height > 300 or img.width > 300:
#                output_size = (300, 300)                 
#                img.thumbnail(output_size)               
#                img.save(self.profile_picture.path) 


# ############################## ChapterXIV topic Inscribing the Transactional Scrolls ##############################
    


# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# from django.urls import reverse


# class Category(models.Model):
    
#     name = models.CharField(max_length=200, db_index=True)   
#     slug = models.SlugField(max_length=200, unique=True)    

#     class Meta:
#         ordering = ('name',) 
#         verbose_name = 'category' 
#         verbose_name_plural = 'categories' 

#     def __str__(self):
        
#         return self.name       


# class Product(models.Model):
   
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
   
#     name = models.CharField(max_length=200, db_index=True)  
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)  
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null = True)   
#     description = models.TextField(blank=True)  
#     price = models.DecimalField(max_digits=10, decimal_places=2)  
#     available = models.BooleanField(default=True)  
#     created = models.DateTimeField(auto_now_add=True)   #
#     updated = models.DateTimeField(auto_now=True)
   
#     class Meta:
#         ordering = ('name',) 
#         indexes = [
#             models.Index(fields=['id', 'slug']), 
#         ]

#     def __str__(self):
#         return self.name
    

#     def get_absolute_url(self):
#         from django.urls import reverse
#         return reverse("product_detail", args=[self.id , self.slug])




# class UserProfile(models.Model):
#     """
#     Extends the Django User model with additional profile information.
#     This model holds custom data for each user, linked via a OneToOneField.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # <--- The One-to-One link   
#     phone_number = models.CharField(max_length=20, blank=True, null=True)   
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)   
#     country = models.CharField(max_length=100, blank=True, null=True)   
#     profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)
   

#     def __str__(self):   
             
#         return f'{self.user.username} Profile'
    
#     def save(self, *args, **kwargs):
        
#         super().save(*args, **kwargs)      
#         if self.profile_picture:             
#             img = Image.open(self.profile_picture.path)          
#             if img.height > 300 or img.width > 300:
#                output_size = (300, 300)                 
#                img.thumbnail(output_size)               
#                img.save(self.profile_picture.path) 



# class Order(models.Model):
#     user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE) # <--- NEW: Link to User model
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False) # <--- NEW: To track if the order is paid

#     class Meta:
#         ordering = ('-created',) # <--- NEW: Order by most recent orders first

#     def __str__(self):
#         return f'Order {self.id} by {self.user.username}'

#     def get_total_cost(self): # <--- NEW: Method to calculate total cost of the order
#         # Sums the cost of all related OrderItem objects
#         return sum(item.get_cost() for item in self.items.all())

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) # <--- NEW: Link to Order model
#     product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE) # <--- NEW: Link to Product model
#     price = models.DecimalField(max_digits=10, decimal_places=2) # <--- NEW: Price at time of purchase (for historical accuracy)
#     quantity = models.PositiveIntegerField(default=1) # <--- NEW: Quantity of the product in this order item

#     class Meta: # <--- NEW: Meta options for OrderItem
#         ordering = ('id',) # <--- NEW: Default ordering for consistency

#     def __str__(self):
#         return f'{self.id}'

#     def get_cost(self): # <--- NEW: Method to calculate cost of a single order item
#         return self.price * self.quantity


# # --- NEW: Cart and CartItem Models ---
# class Cart(models.Model):
#     # A cart can be linked to a user, or exist for an anonymous session (user=None)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('-created_at',)
#         verbose_name = 'cart'
#         verbose_name_plural = 'carts'

#     def __str__(self):
#         if self.user:
#             return f"Cart of {self.user.username}"
#         return f"Anonymous Cart {self.id}"

#     def get_total_price(self):
#         # Calculate the total price of all items in the cart
#         return sum(item.get_cost() for item in self.items.all())



# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2) # Store price at time of adding to cart

#     class Meta:
#         unique_together = ('cart', 'product') # A product can only appear once per cart
#         ordering = ('id',)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"

#     def get_cost(self):
#         # Calculate the total cost for this specific cart item
#         return self.price * self.quantity
# # --- END NEW: Cart and CartItem Models ---





######################################### Chapter XV topic 15.5: The Final Incantation: Implementing Checkout############################ 



from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
import uuid
from decimal import Decimal


class Category(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)   
    slug = models.SlugField(max_length=200, unique=True)    

    class Meta:
        ordering = ('name',) 
        verbose_name = 'category' 
        verbose_name_plural = 'categories' 

    def __str__(self):
        
        return self.name       


class Product(models.Model):
   
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
   
    name = models.CharField(max_length=200, db_index=True)  
    slug = models.SlugField(max_length=200, db_index=True, unique=True)  
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null = True)   
    description = models.TextField(blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    available = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_now_add=True)   #
    updated = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ('name',) 
        indexes = [
            models.Index(fields=['id', 'slug']), 
        ]

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", args=[self.id , self.slug])




class UserProfile(models.Model):
    """
    Extends the Django User model with additional profile information.
    This model holds custom data for each user, linked via a OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) # <--- The One-to-One link   
    phone_number = models.CharField(max_length=20, blank=True, null=True)   
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)   
    country = models.CharField(max_length=100, blank=True, null=True)   
    profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)
   

    def __str__(self):   
             
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)      
        if self.profile_picture:             
            img = Image.open(self.profile_picture.path)          
            if img.height > 300 or img.width > 300:
               output_size = (300, 300)                 
               img.thumbnail(output_size)               
               img.save(self.profile_picture.path) 


# New Update 
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)    
    total_price = models.DecimalField(max_digits=10, 
                                      decimal_places=2, default=Decimal('0.00'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='Pending') 

    
    shipping_address_line1 = models.CharField(max_length=255, blank=True, null=True)
    shipping_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) # <--- NEW: Link to Order model
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE) # <--- NEW: Link to Product model
    price = models.DecimalField(max_digits=10, decimal_places=2) # <--- NEW: Price at time of purchase (for historical accuracy)
    quantity = models.PositiveIntegerField(default=1) # <--- NEW: Quantity of the product in this order item

    class Meta: # <--- NEW: Meta options for OrderItem
        ordering = ('id',) # <--- NEW: Default ordering for consistency

    def __str__(self):
        return f'{self.id}'

    def get_cost(self): # <--- NEW: Method to calculate cost of a single order item
        return self.price * self.quantity


# --- NEW update : Cart and CartItem Models ---
class Cart(models.Model):
    # MODIFIED: Use a UUID as primary key for robust session-based carts
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # A cart can be linked to a user, or exist for an anonymous session (user=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart') # Changed to OneToOneField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        return f"Anonymous Cart {self.id}" # Now uses UUID

    def get_total_price(self):
        # Calculate the total price of all items in the cart
        return sum(item.get_cost() for item in self.items.all())



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Store price at time of adding to cart

    class Meta:
        unique_together = ('cart', 'product') # A product can only appear once per cart
        ordering = ('id',)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Cart {self.cart.id}"

    def get_cost(self):        
        return self.price * self.quantity


