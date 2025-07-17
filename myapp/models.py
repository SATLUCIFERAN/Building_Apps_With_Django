
from django.db import models # Essential import for defining models
from django.db.models import Index

# class Category(models.Model):
#     """
#     Represents a product category in our e-commerce store.
#     This will correspond to a table named 'myapp_category' in the database.
#     """
#     name = models.CharField(max_length=200, db_index=True)
#     # Logic & Imagination: 'name' is a section on our Category Scroll for text,
#     # limited to 200 characters, and indexed for quick searching.

#     slug = models.SlugField(max_length=200, unique=True)
#     # Logic & Imagination: 'slug' is a unique, web-friendly identifier,
#     # like a magical shorthand for the category name, ensuring no two are alike.

#     class Meta:
#         ordering = ('name',) # Logic & Imagination: Always sort categories by name.
#         verbose_name = 'category' # Logic & Imagination: Singular, readable name for admin.
#         verbose_name_plural = 'categories' # Logic & Imagination: Plural, readable name for admin.

#     def __str__(self):
#         """
#         Returns a string representation of the Category object.
#         This is what will be displayed in the Django Admin and when printing Category objects.
#         """
#         return self.name
#         # Logic & Imagination: When Django asks, "What is this Category Scroll called?",
#         # we respond with the name inscribed on it.


# class Product(models.Model):
#     """
#     Represents a product in our e-commerce store.
#     Each product belongs to a Category.
#     """
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
#     # Logic & Imagination: This is a magical thread connecting a Product Scroll
#     # to its specific Category Scroll. If the Category Scroll is ever destroyed,
#     # all connected Product Scrolls are also safely removed.

#     name = models.CharField(max_length=200, db_index=True)
#     # Logic & Imagination: Product's name, indexed for searching.

#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     # Logic & Imagination: Unique, web-friendly identifier for the product.

#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
#     # Logic & Imagination: A section for a product image, stored in a specific
#     # magically organized folder based on upload date. Optional.

#     description = models.TextField(blank=True)
#     # Logic & Imagination: A large section for detailed product information. Optional.

#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     # Logic & Imagination: The product's price, precise to two decimal places,
#     # with a maximum of 10 digits total.

#     available = models.BooleanField(default=True)
#     # Logic & Imagination: A toggle switch indicating if the product is currently
#     # available for purchase. By default, it's available.

#     created = models.DateTimeField(auto_now_add=True)
#     # Logic & Imagination: Automatically records the exact moment the product scroll
#     # was first created.

#     updated = models.DateTimeField(auto_now=True)
#     # Logic & Imagination: Automatically updates the timestamp every time the
#     # product scroll is modified.

#     class Meta:
#         ordering = ('name',) # Logic & Imagination: Always sort products by name.
#         indexes = [
#             models.Index(fields=['id', 'slug']), # <--- CHANGE THIS LINE!
#         ]

#     def __str__(self):
#         return self.name
#         # Logic & Imagination: When asked, "What is this Product Scroll called?",
#         # we respond with its name.
    


############################## Chapter X Part5 topics 12.15  Profile Model ###########################

# myapp/models.py (updated for UserProfile)

# from django.db import models
# from django.contrib.auth.models import User # <--- NEW: Import Django's built-in User model
# from PIL import Image # <--- NEW: Import Image for image processing (install Pillow if not already)


# class Category(models.Model):
    
#     name = models.CharField(max_length=200, db_index=True)   
#     slug = models.SlugField(max_length=200, unique=True)    

    # class Meta:
    #     ordering = ('name',) 
    #     verbose_name = 'category' 
    #     verbose_name_plural = 'categories' 

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
        

# # ... (Product and Category models as before) ...

# class UserProfile(models.Model):
#     """
#     Extends the Django User model with additional profile information.
#     This model holds custom data for each user, linked via a OneToOneField.
#     """
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # <--- The One-to-One link
#     # Detailed Explanation: This is the core of the relationship.
#     # `models.OneToOneField(User, ...)` establishes a one-to-one link to Django's default User model.
#     # `on_delete=models.CASCADE`: This is a crucial database constraint. It means that if the associated
#     # User object is ever deleted from the database, this UserProfile object will also be automatically
#     # deleted. This prevents "orphan" profile entries and maintains data integrity.
#     # Logic & Imagination: This is the unbreakable magical thread binding this
#     # personalized scroll directly to a specific page in the Alchemist's Register (User model).
#     # If the main page is ever destroyed (user deleted), this scroll is also dissolved,
#     # ensuring no fragmented records remain.

#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     # Detailed Explanation: A standard character field for storing a phone number.
#     # `max_length=20`: Sets the maximum length of the string.
#     # `blank=True`: Allows this field to be left empty in Django forms.
#     # `null=True`: Allows the database column to store NULL values. This is important for optional fields.
#     # Logic & Imagination: A dedicated space on the scroll for the customer's magical communication crystal number.

#     address = models.CharField(max_length=255, blank=True, null=True)
#     # Detailed Explanation: A character field for a street address.
#     # Logic & Imagination: A detailed inscription of the customer's primary magical dwelling.

#     city = models.CharField(max_length=100, blank=True, null=True)
#     # Detailed Explanation: A character field for the city.
#     # Logic & Imagination: The name of the magical city where the dwelling resides.

#     country = models.CharField(max_length=100, blank=True, null=True)
#     # Detailed Explanation: A character field for the country.
#     # Logic & Imagination: The enchanted realm or country of the customer.

#     profile_picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)
#     # Detailed Explanation: This is a specialized field for handling image uploads.
#     # `ImageField`: Django's field type for storing image files. It stores the file path in the database.
#     # `default='profile_pics/default.jpg'`: Specifies a default image path. If a user doesn't upload a picture, this image will be used.
#     #    IMPORTANT: You will need to physically create this `default.jpg` file in `media/profile_pics/` later.
#     # `upload_to='profile_pics'`: Tells Django to store uploaded image files in a subdirectory named `profile_pics`
#     #    within your project's `MEDIA_ROOT` directory (which we configured in Chapter XI).
#     # `blank=True`, `null=True`: Makes the field optional.
#     # Logic & Imagination: A magical portrait of the customer, stored in a special
#     # enchanted gallery ('profile_pics'). A default portrait is used if none is provided,
#     # ensuring every personalized scroll has a visual representation.

#     # You can add more fields here, e.g., date_of_birth, magical_specialty, etc.

#     def __str__(self):
#         # Detailed Explanation: This method defines the string representation of a UserProfile object.
#         # When you print a UserProfile object or view it in the Django Admin, this is what will be displayed.
#         # `self.user.username`: Accesses the username of the linked User object.
#         # Logic & Imagination: How the scribe summarizes this personalized scroll when asked for its essence:
#         # "This is the profile scroll belonging to [customer's magical sigil]."
#         return f'{self.user.username} Profile'

#     # Optional: Override save method to resize images
#     def save(self, *args, **kwargs):
#         # Detailed Explanation: We are overriding the default `save` method of the model.
#         # This allows us to add custom logic that executes every time a UserProfile object
#         # is saved to the database (both on creation and update).
#         super().save(*args, **kwargs) # Call the original save method first
#         # Detailed Explanation: This line is absolutely CRITICAL. It calls the `save` method
#         # of the parent class (`models.Model`). This performs the actual database save operation.
#         # It ensures that the UserProfile object (and critically, its `profile_picture` file)
#         # exists on disk *before* we try to open and manipulate the image. Without this,
#         # `Image.open()` would fail because the file wouldn't exist yet.
#         # Logic & Imagination: The scribe first ensures the personalized scroll is securely
#         # placed in its designated spot in the archives. Only then can they proceed with
#         # refining its contents, such as the magical portrait.

#         if self.profile_picture: # Only process if a profile picture has been uploaded
#             # Detailed Explanation: Checks if the `profile_picture` field actually contains a file.
#             img = Image.open(self.profile_picture.path) # Open the image using Pillow
#             # Detailed Explanation: `self.profile_picture.path` provides the absolute file system path
#             # to the uploaded image file. `Image.open()` from the Pillow library loads this image into memory.
#             # Logic & Imagination: The scribe carefully unrolls the magical portrait scroll to inspect it.

#             if img.height > 300 or img.width > 300: # Check if the image is larger than 300x300 pixels
#                 # Detailed Explanation: This condition checks if either the height or width of the image
#                 # exceeds our desired maximum dimension of 300 pixels.
#                 output_size = (300, 300) # Define the target size
#                 img.thumbnail(output_size) # Resize the image, maintaining aspect ratio
#                 # Detailed Explanation: `img.thumbnail(output_size)` is a Pillow method that resizes the image
#                 # in place. It scales the image down (if it's larger than `output_size`) to fit within the
#                 # specified dimensions while preserving the original aspect ratio. This prevents distortion.
#                 # Logic & Imagination: The scribe ensures the magical portrait is not excessively large,
#                 # using a resizing spell to perfectly fit it into a standard 'gallery size' if needed.
#                 # This saves valuable space in the enchanted gallery and makes it quicker to display.

#                 img.save(self.profile_picture.path) # Save the resized image back to the same path
#                 # Detailed Explanation: This line saves the (potentially resized) image back to the
#                 # original file path, overwriting the larger version. This is a common and effective
#                 # optimization for user-uploaded images, as it saves disk space and improves loading
#                 # performance for web pages.
#                 # Logic & Imagination: The scribe carefully re-seals the refined portrait, ensuring
#                 # its new, optimized form is permanently recorded.





############################## Chapter XIII  topics 12.1513.1  Adding ImageField to the Product Model ###########################

# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# from django.urls import reverse # <--- NEW/MODIFIED: Import reverse for get_absolute_url

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
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True) # <--- NEW: ImageField for product
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         # The 'indexes' attribute must be a list of models.Index objects.
#         # Corrected from previous error: ensure no extra tuples or rogue elements.
#         indexes = [ # <--- NEW/MODIFIED: Use 'indexes' instead of 'index_together'
#             models.Index(fields=['id', 'slug']), # <--- NEW/MODIFIED: Define index using models.Index
#         ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self): # <--- NEW: Method to get the product's URL
#         return reverse('product_detail', args=[self.id, self.slug])

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
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
#                 output_size = (300, 300)
#                 img.thumbnail(output_size)
#                 img.save(self.profile_picture.path)



############################## ChapterXIV topic Inscribing the Transactional Scrolls ##############################
    
# myapp/models.py (updated with Order and OrderItem models)

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

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
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         indexes = [
#             models.Index(fields=['id', 'slug']),
#         ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('product_detail', args=[self.id, self.slug])

# # --- NEW: Order and OrderItem Models ---
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
# # --- END NEW: Order and OrderItem Models ---

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
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
#                 output_size = (300, 300)
#                 img.thumbnail(output_size)
#                 img.save(self.profile_picture.path)
                



############################################ ChapterXV Defining Cart and CartItem Models ########################################

# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image
# from django.urls import reverse
# from decimal import Decimal

# # ... (Your existing Category, Product, Order, OrderItem, UserProfile models) ...

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
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         indexes = [
#             models.Index(fields=['id', 'slug']),
#         ]

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('product_detail', args=[self.id, self.slug])

# # --- NEW: Order and OrderItem Models ---
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
# # --- END NEW: Order and OrderItem Models ---

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
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
#                 output_size = (300, 300)
#                 img.thumbnail(output_size)
#                 img.save(self.profile_picture.path)



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




########################################### Chapter XV topic15.5 upddate Proceed to Checkout ##################################### 


from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from decimal import Decimal
import uuid # IMPORTED: Required for UUIDField in Cart

# UserProfile model (retained and correctly placed)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

# Category model (retained)
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Assuming you have a URL pattern named 'product_list_by_category'
        return reverse('product_list_by_category', args=[self.slug])

# Product model (retained)
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) # Added unique=True for slug
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField() # You removed this, keeping it removed for now
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

    # Added save method to auto-generate slug if not present
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# --- NEW: Cart and CartItem Models (MODIFIED for UUID primary key) ---

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
        # Calculate the total cost for this specific cart item
        return self.price * self.quantity
# --- END NEW: Cart and CartItem Models ---


# --- NEW: Order and OrderItem Models (MODIFIED: Added total_price field) ---

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
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
# --- END NEW: Order and OrderItem Models ---