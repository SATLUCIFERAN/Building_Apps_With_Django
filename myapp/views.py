# myapp/views.py

# from django.shortcuts import render # <--- Make sure 'render' is imported
# from django.http import HttpResponse # Keep this for now, but we'll primarily use render
# import datetime # <--- Import datetime module

# def index(request):
#     """
#     This view now renders an HTML template with dynamic data.
#     """
#     # Prepare dynamic data to send to the template
#     context = {
#         'name': 'Alchemist', # Logic & Imagination: This is the name we'll infuse into the {{ name }} rune.
#         'current_datetime': datetime.datetime.now() # Logic & Imagination: This is the time we'll infuse.
#     }
#     # Logic & Imagination: The 'context' dictionary is like a small magical pouch
#     # filled with specific data (key-value pairs) that you want to pass to your template.

#     return render(request, 'myapp/index.html', context)
#     # Logic & Imagination: render() is a powerful magical shortcut.
#     # It takes the user's request, finds the specified template ('myapp/index.html'),
#     # infuses it with the data from our 'context' pouch, and then
#     # conjures the complete HTML page to send back.



################################## for chapter X #################################

# from django.shortcuts import render
# import datetime

# def index(request):
#     context = {
#         'name': 'Alchemist',
#         'current_datetime': datetime.datetime.now(),
#         'magical_items': [ # <--- NEW: List of items
#             {'name': 'Phoenix Feather', 'rarity': 'Rare'},
#             {'name': 'Dragon Scale', 'rarity': 'Legendary'},
#             {'name': 'Unicorn Horn', 'rarity': 'Epic'},
#             {'name': 'Goblin Toe', 'rarity': 'Common'},
#         ],
#         'show_secret_message': True # <--- NEW: A boolean variable for conditional display
#     }
#     return render(request, 'myapp/index.html', context)





#################### ChapterX(10.7.1) ListView: Displaying a Catalog of Scrolls  ####################
# myapp/views.py (updated for ListView)

# from django.shortcuts import render # Keep render for other views or future use
# from django.views.generic import ListView # <--- Import ListView
# from .models import Product, Category # <--- Ensure Product and Category are imported

# class ProductListView(ListView):
#     """
#     Displays a list of all available products.
#     Uses Django's ListView to automatically handle fetching products.
#     """
#     model = Product # <--- Tell ListView which Model to work with
#     template_name = 'myapp/product_list.html' # <--- Specify the template to render
#     context_object_name = 'products' # <--- Name for the list of objects in the template
#     # Logic & Imagination: We're telling our Catalog Conjurer:
#     # 1. "Operate on 'Product' scrolls." (model = Product)
#     # 2. "Use 'product_list.html' as the enchanted display." (template_name)
#     # 3. "Call the list of products 'products' when you infuse the display." (context_object_name)

#     def get_queryset(self):
#         """
#         Optionally filter the queryset (e.g., only show available products).
#         """
#         # By default, ListView would return Product.objects.all().
#         # Here, we can add custom filtering.
#         return Product.objects.filter(available=True)
#         # Logic & Imagination: This is an optional refinement to our Catalog Conjurer.
#         # We're telling it: "Before you list all products, apply a filter:
#         # only show me the scrolls where the 'available' toggle is set to TRUE."




#################### ChapterX(10.7.2) ListView: DetailView ####################

# myapp/views.py (updated for DetailView)

# from django.shortcuts import render
# from django.views.generic import ListView, DetailView # <--- Import DetailView
# from .models import Product, Category

# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     def get_queryset(self):
#         return Product.objects.filter(available=True)

# class ProductDetailView(DetailView):
#     """
#     Displays the details of a single product.
#     Uses Django's DetailView to automatically fetch the product by slug.
#     """
#     model = Product
#     template_name = 'myapp/product_detail.html' # <--- Specify the template to render
#     context_object_name = 'product' # <--- Name for the single object in the template
#     # By default, DetailView looks for 'pk' (primary key) or 'slug' in the URL.
#     # Since our Product model has a slug, we'll use that.
#     # Logic & Imagination: We're telling our Scroll Revealer:
#     # 1. "Operate on 'Product' scrolls." (model = Product)
#     # 2. "Use 'product_detail.html' as the enchanted display." (template_name)
#     # 3. "Call the single product 'product' when you infuse the display." (context_object_name)




#################### ChapterX(10.8) Add Pagination ####################

# myapp/views.py (updated for Pagination)

# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import Product, Category

# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6 # <--- NEW: Display 6 products per page
#     # Logic & Imagination: Tell the Catalog Conjurer to only show 6 Product Scrolls per enchanted page.

#     def get_queryset(self):
#         return Product.objects.filter(available=True)

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'






#################### ChapterX(11.5) Handle the search Query ####################

# from django.shortcuts import render, redirect 
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from django.db.models import Q 

# from .forms import ContactForm # We will import this AFTER forms.py is created

# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
       
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q') 

#         if query:            
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query) 
#             )
            
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'



######################### ChapterX(11.6) Django Form ###########################

# myapp/views.py (updated for ContactForm)

# from django.shortcuts import render, redirect # <--- Add redirect for successful form submission
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from django.db.models import Q
# from .forms import ContactForm # <--- NEW: Import your ContactForm (now that forms.py exists!)

# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):
#     """
#     Handles the contact form submission.
#     """
#     if request.method == 'POST':
#         # Logic & Imagination: The customer has just clicked the "Seal and Deliver" button,
#         # sending their filled inquiry parchment (a POST request) to your laboratory.

#         form = ContactForm(request.POST) # Bind the POST data to the form
#         # Logic & Imagination: You've taken the customer's freshly filled parchment (request.POST)
#         # and handed it to your magical Form-Building Spell (ContactForm) for initial processing.
#         # This 'binding' means the form instance now contains the data the user submitted.

#         if form.is_valid():
#             # Logic & Imagination: The Form-Building Spell is now inspecting the parchment.
#             # It's checking every inscription to see if it's correct, complete, and legible
#             # according to the rules you defined in forms.py (e.g., is the email format valid?
#             # is the name too long?). If all checks pass, the spell declares the parchment "valid."

#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Here you would typically send an email or save to a database
#             print(f"New contact message from {name} ({email}): {message}")
#             # Logic & Imagination: The spell has successfully extracted the clean, validated,
#             # and magically purified information from the parchment into a neat bundle
#             # called 'cleaned_data'. Now, you, the Alchemist, can safely use this information
#             # (e.g., send a magical raven with the message to your support team,
#             # or record it in a secure ledger).

#             # Redirect to a success page or back to the same page with a success message
#             return redirect('product_list') # Redirect to product list for now
#             # Logic & Imagination: After successfully processing the inquiry, you redirect
#             # the customer's browser to another location (like the product list),
#             # signaling that their message was received and handled. This is the
#             # "Post/Redirect/Get" pattern, which prevents duplicate submissions.
#         else:
#             # Logic & Imagination: Oh no! The Form-Building Spell detected errors on the parchment.
#             # Some inscriptions are missing, or their magical format is incorrect.
#             # The 'form' object now holds magical glowing indicators of where the errors are,
#             # ready to be shown back to the customer.
#             pass # The template will display the errors automatically

#     else: # request.method == 'GET'
#         # Logic & Imagination: The customer has just arrived at the contact page,
#         # asking for a blank inquiry parchment (a GET request).

#         form = ContactForm() # Create an empty form instance
#         # Logic & Imagination: You've conjured a fresh, blank inquiry parchment for the customer,
#         # ready for them to fill with their magical quill.

#     return render(request, 'myapp/contact.html', {'form': form})
#     # Logic & Imagination: You're now rendering the contact template. You pass the 'form' object
#     # (either a blank one or one filled with user data and error messages) to the template.
#     # The template will then use this object to magically draw the form on the customer's screen.






######################### ChapterXII part 2 topic 12.6 User Registration ################################

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from django.db.models import Q
# from .forms import ContactForm
# from django.contrib.auth.forms import UserCreationForm # <--- NEW: Import Django's UserCreationForm
# from django.contrib.auth import login as auth_login # <--- NEW: Import Django's login function (aliased to avoid name conflict)

# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 

#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# # ... (ProductListView and ProductDetailView classes as before) ...
# # ... (contact_view function as before) ...

# def register(request):
#     """
#     Handles user registration.
#     """
#     if request.method == 'POST':
#         # Logic & Imagination: A new traveler has submitted their initiation declarations.
#         form = UserCreationForm(request.POST) # Bind the POST data to the form
#         # Logic & Imagination: The Initiation Scribe (UserCreationForm) takes the declarations
#         # and prepares them for validation.

#         if form.is_valid():
#             # Logic & Imagination: The Scribe verifies all declarations. If they are
#             # unique and correctly formatted (e.g., password meets complexity rules),
#             # the ritual proceeds.
#             user = form.save() # Save the new user to the database
#             # Logic & Imagination: The Scribe inscribes the new identity into the Register.
#             # A new page is created for this customer.

#             auth_login(request, user) # Log the user in immediately after registration
#             # Logic & Imagination: Immediately after initiation, the doorkeeper grants
#             # the new customer their Access Amulet (logs them in), so they don't have
#             # to present credentials again right away.

#             return redirect('product_list') # Redirect to a success page (e.g., product list)
#             # Logic & Imagination: The newly initiated customer is guided into the main
#             # marketplace, ready to explore.
#         else:
#             # Logic & Imagination: The Scribe found errors in the declarations (e.g.,
#             # username already taken, password too weak). The form now holds glowing
#             # error indicators to guide the traveler to correct their declarations.
#             pass # Form will contain errors to display in template

#     else: # request.method == 'GET'
#         # Logic & Imagination: A new traveler approaches, asking for the blank
#         # initiation parchment.
#         form = UserCreationForm() # Create an empty form instance
#         # Logic & Imagination: The Initiation Scribe provides a fresh, blank parchment.

#     return render(request, 'myapp/register.html', {'form': form})
#     # Logic & Imagination: The 'register.html' template is conjured, displaying
#     # the initiation parchment (either blank or with errors).





########################## Chapter XII Part 2 topic 12.7 Update for user login ###################################


# myapp/views.py (updated for User Login)

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # <--- NEW: Import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout # <--- NEW: Import logout function


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_detail.html'
    context_object_name = 'product'

def contact_view(request):

    if request.method == 'POST':      
        form = ContactForm(request.POST)       
        if form.is_valid():      
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']           
            print(f"New contact message from {name} ({email}): {message}")         
           
            return redirect('product_list') 
  
        else:            
            pass 
        
    else:         
        form = ContactForm() 
        
    return render(request, 'myapp/contact.html', {'form': form})
    

def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':        
        form = UserCreationForm(request.POST)        

        if form.is_valid():            
            user = form.save()          
            auth_login(request, user)             

            return redirect('product_list')             
        else:          
            pass 

    else:     
        form = UserCreationForm()         

    return render(request, 'myapp/register.html', {'form': form})
    

# ... (ProductListView and ProductDetailView classes as before) ...
# ... (contact_view function as before) ...
# ... (register function as before) ...


def user_login(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        # Logic & Imagination: A customer is presenting their credentials for verification.
        form = AuthenticationForm(request, data=request.POST) # Bind request and POST data
        # Logic & Imagination: The doorkeeper (AuthenticationForm) takes the presented
        # sigil and incantation, ready to verify.

        if form.is_valid():
            # Logic & Imagination: The doorkeeper verifies the credentials against the Register.
            # If they match, the customer is deemed authentic.
            user = form.get_user() # Get the authenticated user object
            # Logic & Imagination: The doorkeeper identifies the specific customer from the Register.

            auth_login(request, user) # Log the user in
            # Logic & Imagination: The doorkeeper bestows the "Amulet of Active Presence"
            # (logs the user in), allowing them free passage.

            return redirect('product_list') # Redirect to a success page
            # Logic & Imagination: The authenticated customer is guided into the main marketplace.
        else:
            # Logic & Imagination: The doorkeeper found the credentials to be incorrect
            # or incomplete. The form now holds glowing error indicators.
            pass # Form will contain errors to display in template

    else: # request.method == 'GET'
        # Logic & Imagination: A customer approaches, asking for the login parchment.
        form = AuthenticationForm() # Create an empty form instance
        # Logic & Imagination: The doorkeeper provides a fresh login parchment.

    return render(request, 'myapp/login.html', {'form': form})
    # Logic & Imagination: The 'login.html' template is conjured, displaying
    # the login parchment.




########################## Chapter XII Part 2 topic 12.8 Update for user logout ###################################

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from django.db.models import Q
# from .forms import ContactForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout # logout is now imported


# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):
#     """
#     Handles user registration.
#     """
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):
#     """
#     Handles user login.
#     """
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    

# # ... (ProductListView, ProductDetailView, contact_view, register, user_login functions as before) ...

# def user_logout(request):
#     """
#     Logs the user out.
#     """
#     auth_logout(request) # Perform the logout
#     # Logic & Imagination: The doorkeeper takes back the "Amulet of Active Presence."

#     return redirect('product_list') # Redirect to a page after logout (e.g., product list)
#     # Logic & Imagination: The customer is guided back to the public entrance of the marketplace.




# ########################### Chapter XII Part 3  Add Home Page ###################################

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from django.db.models import Q
# from .forms import ContactForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout # logout is now imported


# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list')   
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):   
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):    
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    


# def user_logout(request):   
#     auth_logout(request)     

#     return redirect('product_list') 
    
# # ... (ProductListView class as before) ...
# # ... (ProductDetailView class as before) ...
# # ... (contact_view function as before) ...
# # ... (register function as before) ...
# # ... (user_login function as before) ...
# # ... (user_logout function as before) ...


# def home_view(request):
#     """
#     Renders the home page of the store.
#     """
#     # Logic & Imagination: This view is the magical greeter at the main entrance.
#     # Its sole purpose is to conjure the grand welcome hall template.
#     return render(request, 'myapp/home.html', {}) # Pass an empty context for now



############################ Chapter XII Part4 updated for @login_required profile view ###################################

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required # <--- NEW: Import login_required decorator


# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):
#     """
#     Handles user registration.
#     """
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):
#     """
#     Handles user login.
#     """
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    

# # ... (ProductListView, ProductDetailView, contact_view, register, user_login functions as before) ...

# def user_logout(request):
#     """
#     Logs the user out.
#     """
#     auth_logout(request) # Perform the logout
#     # Logic & Imagination: The doorkeeper takes back the "Amulet of Active Presence."

#     return redirect('product_list') # Redirect to a page after logout (e.g., product list)
#     # Logic & Imagination: The customer is guided back to the public entrance of the marketplace.


# def home_view(request):
#     """
#     Renders the home page of the store.
#     """
#     # Logic & Imagination: This view is the magical greeter at the main entrance.
#     # Its sole purpose is to conjure the grand welcome hall template.
#     return render(request, 'myapp/home.html', {}) # Pass an empty context for now


# @login_required # <--- Make sure this decorator is here
# def profile_view(request): # <--- Make sure this function is present and correctly named
#     """
#     Displays the user's profile page (only accessible to logged-in users).
#     """
#     return render(request, 'myapp/profile.html', {})






############################ ChapterXII(Part4) Topic 12.11 LoginRequiredMixin   ###################################


# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, View # <--- RE-EMPHASIZED: Import View for generic CBV
# from .models import Product, Category
# from .forms import ContactForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin # <--- NEW: Import LoginRequiredMixin


# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):
#     """
#     Handles user registration.
#     """
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):
#     """
#     Handles user login.
#     """
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    

# def user_logout(request):    
#     auth_logout(request)   

#     return redirect('product_list') 


# def home_view(request):    
    
#     return render(request, 'myapp/home.html', {}) 


# @login_required 
# def profile_view(request): 
   
#     return render(request, 'myapp/profile.html', {})



# class OrderHistoryView(LoginRequiredMixin, View): # <--- Inherit from LoginRequiredMixin and View
#     """
#     Displays the user's order history (only accessible to logged-in users).
#     """
#     # Logic & Imagination: This is the customer's personal order ledger chamber.
#     # By inheriting LoginRequiredMixin, this chamber inherently possesses the
#     # authentication ward.
#     def get(self, request, *args, **kwargs):
#         # In a real app, you'd fetch orders for request.user here
#         orders = [
#             {'id': 1, 'item': 'Elixir of Strength', 'date': '2025-01-15', 'total': 25.00},
#             {'id': 2, 'item': 'Potion of Invisibility', 'date': '2025-03-22', 'total': 40.00},
#         ]
#         return render(request, 'myapp/order_history.html', {'orders': orders})
    



############################ ChapterXII(Part4) Topic12.12 Access to Staff/Superusers    ###################################

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, View
# from .models import Product, Category
# from .forms import ContactForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.admin.views.decorators import staff_member_required # <--- NEW: Import staff_member_required


# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):
    
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):
    
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    

# def user_logout(request):    
#     auth_logout(request)   

#     return redirect('product_list') 


# def home_view(request):    
    
#     return render(request, 'myapp/home.html', {}) 


# @login_required 
# def profile_view(request): 
   
#     return render(request, 'myapp/profile.html', {})



# class OrderHistoryView(LoginRequiredMixin, View): 
   
#     def get(self, request, *args, **kwargs):
#         # In a real app, you'd fetch orders for request.user here
#         orders = [
#             {'id': 1, 'item': 'Elixir of Strength', 'date': '2025-01-15', 'total': 25.00},
#             {'id': 2, 'item': 'Potion of Invisibility', 'date': '2025-03-22', 'total': 40.00},
#         ]
#         return render(request, 'myapp/order_history.html', {'orders': orders})
    


# # ... (ProductListView, ProductDetailView, contact_view, register, user_login, 
# # user_logout, profile_view, home_view, OrderHistoryView functions/classes as before) ...

# @staff_member_required # <--- Apply this decorator!
# def vendor_dashboard_view(request):
#     """
#     Displays a dashboard for staff members (vendors).
#     Requires user to be logged in AND is_staff=True.
#     """
#     # Logic & Imagination: This is the view for the Vendor's Secret Guild Hall.
#     # The @staff_member_required ward ensures only those with the "Staff Guild"
#     # enchantment on their amulet can enter.
#     return render(request, 'myapp/vendor_dashboard.html', {})





######################### Chapter XII Part 6 topic 12.18  Crafting the Profile Editing Forms: ###########################

# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, View
# from .models import Product, Category, UserProfile # <-- Ensure UserProfile is imported
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm # <-- NEW: Import new forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib import messages # <-- NEW: Import Django's messages framework



# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )
#         return queryset

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

# def contact_view(request):

#     if request.method == 'POST':      
#         form = ContactForm(request.POST)       
#         if form.is_valid():      
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']           
#             print(f"New contact message from {name} ({email}): {message}")         
           
#             return redirect('product_list') 
  
#         else:            
#             pass 
        
#     else:         
#         form = ContactForm() 
        
#     return render(request, 'myapp/contact.html', {'form': form})
    

# def register(request):
    
#     if request.method == 'POST':        
#         form = UserCreationForm(request.POST)        

#         if form.is_valid():            
#             user = form.save()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:          
#             pass 

#     else:     
#         form = UserCreationForm()         

#     return render(request, 'myapp/register.html', {'form': form})    


# def user_login(request):
    
#     if request.method == 'POST':        
#         form = AuthenticationForm(request, data=request.POST)         

#         if form.is_valid():            
#             user = form.get_user()          
#             auth_login(request, user)           
#             return redirect('product_list')             
#         else:            
#             pass 

#     else:         
#         form = AuthenticationForm()        

#     return render(request, 'myapp/login.html', {'form': form})
    

# def user_logout(request):    
#     auth_logout(request)   

#     return redirect('product_list') 


# def home_view(request):    
    
#     return render(request, 'myapp/home.html', {}) 


# @login_required 
# def profile_view(request): 
   
#     return render(request, 'myapp/profile.html', {})



# class OrderHistoryView(LoginRequiredMixin, View): 
   
#     def get(self, request, *args, **kwargs):
#         # In a real app, you'd fetch orders for request.user here
#         orders = [
#             {'id': 1, 'item': 'Elixir of Strength', 'date': '2025-01-15', 'total': 25.00},
#             {'id': 2, 'item': 'Potion of Invisibility', 'date': '2025-03-22', 'total': 40.00},
#         ]
#         return render(request, 'myapp/order_history.html', {'orders': orders})
    


# # ... (ProductListView, ProductDetailView, contact_view, register, user_login, 
# # user_logout, profile_view, home_view, OrderHistoryView functions/classes as before) ...

# @staff_member_required # <--- Apply this decorator!
# def vendor_dashboard_view(request):
#     """
#     Displays a dashboard for staff members (vendors).
#     Requires user to be logged in AND is_staff=True.
#     """
#     # Logic & Imagination: This is the view for the Vendor's Secret Guild Hall.
#     # The @staff_member_required ward ensures only those with the "Staff Guild"
#     # enchantment on their amulet can enter.
#     return render(request, 'myapp/vendor_dashboard.html', {})




# # ... (All existing views: ProductListView, ProductDetailView, contact_view,
# #      register, user_login, user_logout, home_view, profile_view,
# #      OrderHistoryView, vendor_dashboard_view) ...

# @login_required # Ensure only logged-in users can access this page
# def profile_update_view(request):
#     """
#     Allows authenticated users to update their User and UserProfile information.
#     """
#     # Logic & Imagination: This is the customer's personal desk in their private chamber.
#     # It presents their current records for review and allows them to make new inscriptions.

#     if request.method == 'POST':
#         # Detailed Explanation: If the request method is POST, it means the user has submitted the forms.
#         # We need to bind the submitted data to our form instances.
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         # Detailed Explanation: We create an instance of UserUpdateForm.
#         # `request.POST`: Contains the submitted form data.
#         # `instance=request.user`: This is CRUCIAL. It tells the form to populate itself with the
#         #                           data from the currently logged-in user object (`request.user`)
#         #                           and to save changes *to that existing instance*, not create a new one.
#         # Logic & Imagination: The quill for core identity is loaded with the new inscriptions,
#         # ready to update the customer's main Register page.

#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
#         # Detailed Explanation: We create an instance of ProfileUpdateForm.
#         # `request.POST`: Contains the submitted text data.
#         # `request.FILES`: Contains any uploaded files (like the profile picture). This is essential for ImageField.
#         # `instance=request.user.userprofile`: This is also CRUCIAL. It binds the form to the
#         #                                       existing UserProfile object of the logged-in user.
#         # Logic & Imagination: The versatile quill for personalized scrolls is loaded with new text
#         # and potentially a new magical portrait, ready to update the customer's personalized scroll.

#         if user_form.is_valid() and profile_form.is_valid():
#             # Detailed Explanation: Both forms must pass validation. If they do, their data is clean.
#             user_form.save() # Save changes to the User model
#             profile_form.save() # Save changes to the UserProfile model
#             # Logic & Imagination: If all new inscriptions are valid, the changes are committed
#             # to both the main Register page and the personalized scroll.

#             messages.success(request, f'Your magical profile has been updated!')
#             # Detailed Explanation: Django's messages framework is used to display a success notification
#             # to the user after a successful update. This message will be displayed on the next page.
#             # Logic & Imagination: A shimmering, green magical light appears, confirming the successful
#             # update of the customer's records.

#             return redirect('profile') # Redirect back to the profile view
#             # Detailed Explanation: After a successful update, redirect the user back to their profile page.
#             # This prevents resubmission of the form if the user refreshes the page.
#             # Logic & Imagination: The customer is gently guided back to their updated profile chamber.
#         else:
#             messages.error(request, 'There was an error updating your profile. Please check the form.')
#             # Detailed Explanation: If validation fails for either form, display an error message.
#             # Logic & Imagination: A faint, red magical glow appears, indicating issues with the inscriptions.

#     else: # request.method == 'GET'
#         # Detailed Explanation: If the request method is GET, it means the user is just requesting the page.
#         # We need to pre-populate the forms with the current user's data.
#         user_form = UserUpdateForm(instance=request.user)
#         # Detailed Explanation: Create a UserUpdateForm instance, pre-populated with data from `request.user`.
#         # Logic & Imagination: The customer's quill for core identity is presented, already displaying
#         # their current details from the main Register page.

#         profile_form = ProfileUpdateForm(instance=request.user.userprofile)
#         # Detailed Explanation: Create a ProfileUpdateForm instance, pre-populated with data from
#         # `request.user.userprofile`. This relies on the `user.userprofile` accessor working correctly.
#         # Logic & Imagination: The versatile quill for personalized scrolls is presented,
#         # displaying all the current details from their personalized scroll.

#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form
#     }
#     # Detailed Explanation: Create a dictionary to pass both form instances to the template.

#     return render(request, 'myapp/profile_update.html', context)
#     # Detailed Explanation: Render the new profile update template with the forms.
#     # Logic & Imagination: The 'profile_update.html' template is conjured, displaying
#     # the customer's personal desk with their quills and current records.




############################## ChapterXIV topic 14.1 Implementing Basic Product Search ##############################


# from django.shortcuts import render, redirect, get_object_or_404 # <--- MODIFIED: Added get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView 
# from .models import Product, Category, UserProfile, Order, OrderItem 
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required 
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
# from django.contrib import messages
# from django.urls import reverse_lazy 

# # Home view
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.') # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items(): # <--- NEW/MODIFIED: Loop through errors for detailed messages
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}") # <--- NEW/MODIFIED: Display specific error messages
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!") # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.") # <--- NEW/MODIFIED: Added error message
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.") # <--- NEW/MODIFIED: Added info message
#     return redirect('product_list')

# # User Profile View
# class UserProfileView(LoginRequiredMixin, DetailView): # <--- MODIFIED: Changed from function to Class-Based View
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         # Retrieve the UserProfile for the currently logged-in user
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View

# class UserProfileUpdateView(LoginRequiredMixin, UpdateView): 
#     model = UserProfile
#     form_class = ProfileUpdateForm 
#     template_name = 'myapp/profile_edit.html' 
#     success_url = reverse_lazy('profile_view') # Redirect to profile page on success # <--- MODIFIED: Changed to profile_view

#     def get_object(self):
#         # Ensure only the logged-in user can edit their own profile
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Pass the UserForm for updating User model fields (username, email)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object() # Get the UserProfile instance
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form() # Get the ProfileUpdateForm instance

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form) # Use form_valid for success_url redirect
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form # Pass back invalid user_form
#             context['form'] = profile_form # Pass back invalid profile_form (which is profile_form here)
#             return self.render_to_response(context) # Re-render with errors

# # Order History View

# class OrderHistoryView(LoginRequiredMixin, ListView): 
#     model = Order # <--- NEW: Specify model for ListView
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created'] # Order by most recent orders first # <--- NEW: Ordering for ListView

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # Only show orders for the logged-in user
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View
# class VendorDashboardView(LoginRequiredMixin, ListView): # <--- MODIFIED: Changed from function to ListView, added LoginRequiredMixin
#     model = Product # <--- NEW: Specify model for ListView
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products' # <--- NEW: Context object name for ListView

#     # Use UserPassesTestMixin for staff check
#     def dispatch(self, request, *args, **kwargs): # <--- NEW/MODIFIED: Use dispatch for staff check
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home') # Redirect to home or login page
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # For a real vendor dashboard, you might filter products by the vendor who owns them.
#         # For now, it lists all products for staff members.
#         return Product.objects.all().order_by('-created') # <--- NEW: Ordering for ListView

# # Product List View
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6 # <--- RETAINED: Your original pagination setting

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True) # <--- RETAINED: Your original base queryset
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(
#                 Q(name__icontains=query) |
#                 Q(description__icontains=query)
#             )

    #  # --- Categorical Sifting (NEW for 14.2) ---
    #     category_slug = self.request.GET.get('category') # <--- NEW: Get the category slug from the URL
    #     if category_slug: # <--- NEW: If a category is selected
    #         # Filter products by the selected category's slug
    #         queryset = queryset.filter(category__slug=category_slug) # <--- NEW: Apply category filter
    #     # --- End Categorical Sifting ---
    #     return queryset.order_by('name') # <--- NEW/MODIFIED: Added ordering for consistency

    # def get_context_data(self, **kwargs): # <--- NEW: Override to add categories to context
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all().order_by('name') # <--- NEW: Fetch all categories
    #     # Get the slug of the currently selected category from the URL, if any
    #     selected_category_slug = self.request.GET.get('category') # <--- NEW: Get selected category slug
    #     if selected_category_slug:
    #         context['selected_category_slug'] = selected_category_slug # <--- NEW: Add to context for highlighting
    #     return context


# # Product Detail View
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self): # <--- NEW/MODIFIED: Ensure object retrieval by ID and slug
#         # Retrieve object based on both ID and slug
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])




######################### ChapterXIV topic 14.3 The Price Divination: Filtering by Price Range ######################

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import Product, Category, UserProfile, Order, OrderItem
from django.db.models import Q
from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from decimal import Decimal # <--- NEW: Import Decimal for price handling


# # Home view
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.') # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items(): # <--- NEW/MODIFIED: Loop through errors for detailed messages
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}") # <--- NEW/MODIFIED: Display specific error messages
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!") # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.") # <--- NEW/MODIFIED: Added error message
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.") # <--- NEW/MODIFIED: Added info message
#     return redirect('product_list')

# # User Profile View
# class UserProfileView(LoginRequiredMixin, DetailView): # <--- MODIFIED: Changed from function to Class-Based View
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         # Retrieve the UserProfile for the currently logged-in user
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View

# class UserProfileUpdateView(LoginRequiredMixin, UpdateView): 
#     model = UserProfile
#     form_class = ProfileUpdateForm 
#     template_name = 'myapp/profile_edit.html' 
#     success_url = reverse_lazy('profile_view') # Redirect to profile page on success # <--- MODIFIED: Changed to profile_view

#     def get_object(self):
#         # Ensure only the logged-in user can edit their own profile
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Pass the UserForm for updating User model fields (username, email)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object() # Get the UserProfile instance
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form() # Get the ProfileUpdateForm instance

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form) # Use form_valid for success_url redirect
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form # Pass back invalid user_form
#             context['form'] = profile_form # Pass back invalid profile_form (which is profile_form here)
#             return self.render_to_response(context) # Re-render with errors

# # Order History View

# class OrderHistoryView(LoginRequiredMixin, ListView): 
#     model = Order # <--- NEW: Specify model for ListView
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created'] # Order by most recent orders first # <--- NEW: Ordering for ListView

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # Only show orders for the logged-in user
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View
# class VendorDashboardView(LoginRequiredMixin, ListView): # <--- MODIFIED: Changed from function to ListView, added LoginRequiredMixin
#     model = Product # <--- NEW: Specify model for ListView
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products' # <--- NEW: Context object name for ListView

#     # Use UserPassesTestMixin for staff check
#     def dispatch(self, request, *args, **kwargs): # <--- NEW/MODIFIED: Use dispatch for staff check
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home') # Redirect to home or login page
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # For a real vendor dashboard, you might filter products by the vendor who owns them.
#         # For now, it lists all products for staff members.
#         return Product.objects.all().order_by('-created') # <--- NEW: Ordering for ListView


# # ... (rest of your views: home_view, contact_view, register, user_login, user_logout,
# # UserProfileView, UserProfileUpdateView, OrderHistoryView, VendorDashboardView) ...

# # Product List View (MODIFIED: For search, category, and PRICE filtering)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         # --- Basic Search (from 14.1) ---
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
#         # --- End Basic Search ---

#         # --- Categorical Sifting (from 14.2) ---
#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)
#         # --- End Categorical Sifting ---

#         # --- Price Divination (NEW for 14.3) ---
#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price) # Convert to Decimal for accurate comparison
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")

#         if max_price:
#             try:
#                 max_price = Decimal(max_price) # Convert to Decimal for accurate comparison
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")
#         # --- End Price Divination ---

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')

#         # Preserve current filter values for the template
#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '') # <--- NEW: Pass min_price to template
#         context['max_price'] = self.request.GET.get('max_price', '') # <--- NEW: Pass max_price to template

#         return context


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self): # <--- NEW/MODIFIED: Ensure object retrieval by ID and slug
#         # Retrieve object based on both ID and slug
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])
    







######################### ChapterXIV topic 15.2  Adding Products to the Cart ######################

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem # <--- MODIFIED: Added Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json # <--- NEW: Import json for session data
# import uuid # <--- NEW: Import uuid for anonymous cart ID generation


# # Home view
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.') # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items(): # <--- NEW/MODIFIED: Loop through errors for detailed messages
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}") # <--- NEW/MODIFIED: Display specific error messages
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!") # <--- NEW/MODIFIED: Added success message
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.") # <--- NEW/MODIFIED: Added error message
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.") # <--- NEW/MODIFIED: Added info message
#     return redirect('product_list')

# # User Profile View
# class UserProfileView(LoginRequiredMixin, DetailView): # <--- MODIFIED: Changed from function to Class-Based View
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         # Retrieve the UserProfile for the currently logged-in user
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View

# class UserProfileUpdateView(LoginRequiredMixin, UpdateView): 
#     model = UserProfile
#     form_class = ProfileUpdateForm 
#     template_name = 'myapp/profile_edit.html' 
#     success_url = reverse_lazy('profile_view') # Redirect to profile page on success # <--- MODIFIED: Changed to profile_view

#     def get_object(self):
#         # Ensure only the logged-in user can edit their own profile
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Pass the UserForm for updating User model fields (username, email)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object() # Get the UserProfile instance
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form() # Get the ProfileUpdateForm instance

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form) # Use form_valid for success_url redirect
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form # Pass back invalid user_form
#             context['form'] = profile_form # Pass back invalid profile_form (which is profile_form here)
#             return self.render_to_response(context) # Re-render with errors

# # Order History View

# class OrderHistoryView(LoginRequiredMixin, ListView): 
#     model = Order # <--- NEW: Specify model for ListView
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created'] # Order by most recent orders first # <--- NEW: Ordering for ListView

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # Only show orders for the logged-in user
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View
# class VendorDashboardView(LoginRequiredMixin, ListView): # <--- MODIFIED: Changed from function to ListView, added LoginRequiredMixin
#     model = Product # <--- NEW: Specify model for ListView
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products' # <--- NEW: Context object name for ListView

#     # Use UserPassesTestMixin for staff check
#     def dispatch(self, request, *args, **kwargs): # <--- NEW/MODIFIED: Use dispatch for staff check
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home') # Redirect to home or login page
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self): # <--- NEW/MODIFIED: Override get_queryset for ListView
#         # For a real vendor dashboard, you might filter products by the vendor who owns them.
#         # For now, it lists all products for staff members.
#         return Product.objects.all().order_by('-created') # <--- NEW: Ordering for ListView


# # ... (rest of your views: home_view, contact_view, register, user_login, user_logout,
# # UserProfileView, UserProfileUpdateView, OrderHistoryView, VendorDashboardView) ...

# # Product List View (MODIFIED: For search, category, and PRICE filtering)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         # --- Basic Search (from 14.1) ---
#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
#         # --- End Basic Search ---

#         # --- Categorical Sifting (from 14.2) ---
#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)
#         # --- End Categorical Sifting ---

#         # --- Price Divination (NEW for 14.3) ---
#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price) # Convert to Decimal for accurate comparison
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")

#         if max_price:
#             try:
#                 max_price = Decimal(max_price) # Convert to Decimal for accurate comparison
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")
#         # --- End Price Divination ---

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')

#         # Preserve current filter values for the template
#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '') # <--- NEW: Pass min_price to template
#         context['max_price'] = self.request.GET.get('max_price', '') # <--- NEW: Pass max_price to template

#         return context


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self): # <--- NEW/MODIFIED: Ensure object retrieval by ID and slug
#         # Retrieve object based on both ID and slug
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])
    



# # ... (Your existing home_view, contact_view, register, user_login, user_logout) ...
# # ... (UserProfileView, UserProfileUpdateView, OrderHistoryView, VendorDashboardView) ...
# # ... (ProductListView, ProductDetailView) ...


# # --- NEW: Add to Cart View ---
# def add_to_cart(request, product_id):
#     # Retrieve the product or return a 404 if not found
#     product = get_object_or_404(Product, id=product_id)

#     # Determine the quantity from the POST request, default to 1
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     # --- Cart Identification and Creation ---
#     cart = None
#     if request.user.is_authenticated:
#         # For authenticated users, get or create a cart linked to their user object
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         # For anonymous users, use a session key to identify the cart
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True) # Ensure it's an anonymous cart
#             except Cart.DoesNotExist:
#                 cart = None # Cart ID in session is invalid, create new

#         if not cart:
#             # Create a new anonymous cart and store its ID in the session
#             cart = Cart.objects.create(user=None) # Create cart with no user
#             request.session['cart_id'] = str(cart.id) # Store cart ID in session
#             messages.info(request, "A new anonymous cart was created for your session.")
#     # --- End Cart Identification ---

#     # --- Add/Update CartItem ---
#     # Get or create the CartItem for this product in the identified cart
#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price} # Set initial quantity and current product price
#     )

#     if not created:
#         # If CartItem already exists, update its quantity
#         cart_item.quantity += quantity
#         cart_item.price = product.price # Update price to current product price (optional, but good for consistency)
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     # --- End Add/Update CartItem ---

#     # Redirect back to the product detail page or product list
#     return redirect(product.get_absolute_url())
# # --- END NEW: Add to Cart View ---






######################### ChapterXIV topic 15.3 The Satchel's Glimpse: Displaying Cart Contents ######################


# myapp/views.py (updated with cart_detail view)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json
# import uuid

# # Home view (retained)
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view (retained)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration (retained, with added messages)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.')
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login (retained, with added messages)
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout (retained, with added message)
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('product_list')

# # User Profile View (retained)
# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View (retained)
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = 'myapp/profile_edit.html'
#     success_url = reverse_lazy('profile_view')

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form)
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form
#             context['form'] = profile_form
#             return self.render_to_response(context)

# # Order History View (retained)
# class OrderHistoryView(LoginRequiredMixin, ListView):
#     model = Order
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created']

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View (retained)
# class VendorDashboardView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products'

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.all().order_by('-created')

# # Product List View (retained)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)

#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price)
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")
            
#         if max_price:
#             try:
#                 max_price = Decimal(max_price)
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')
        
#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '')
#         context['max_price'] = self.request.GET.get('max_price', '')
        
#         return context

# # Product Detail View (retained)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self):
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# # Add to Cart View (retained from 15.2)
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     cart = None
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 cart = None
#         if not cart:
#             cart = Cart.objects.create(user=None)
#             request.session['cart_id'] = str(cart.id)
#             messages.info(request, "A new anonymous cart was created for your session.")

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price}
#     )

#     if not created:
#         cart_item.quantity += quantity
#         cart_item.price = product.price
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     return redirect(product.get_absolute_url())

# # --- NEW: Cart Detail View ---
# def cart_detail(request): # NEW function definition for the cart detail page
#     cart = None # NEW variable initialization for the cart object
#     if request.user.is_authenticated: # RETAINED cart identification logic from add_to_cart
#         try:
#             cart = Cart.objects.get(user=request.user) # RETAINED logic to get user's cart
#         except Cart.DoesNotExist: # RETAINED error handling for non-existent cart
#             pass # RETAINED: if cart doesn't exist, 'cart' remains None
#     else: # RETAINED cart identification logic for anonymous users
#         session_cart_id = request.session.get('cart_id') # RETAINED: get cart ID from session
#         if session_cart_id: # RETAINED: if session ID exists
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True) # RETAINED: get anonymous cart
#             except Cart.DoesNotExist: # RETAINED: error handling for non-existent session cart
#                 pass # RETAINED: if cart doesn't exist, 'cart' remains None

#     if not cart: # NEW conditional block: handles scenario where no cart is found (for either user type)
#         cart_items = [] # NEW: Initialize an empty list for cart items
#         total_price = Decimal('0.00') # NEW: Initialize total price to zero
#     else: # NEW: Executes if a cart object was successfully identified
#         cart_items = cart.items.all() # NEW: Fetch all CartItem objects related to the identified cart
#         total_price = cart.get_total_price() # NEW: Calculate the total price of all items in the cart

#     context = { # NEW: Create a dictionary to pass data to the template
#         'cart': cart, # NEW: Add the cart object to the context
#         'cart_items': cart_items, # NEW: Add the list of cart items to the context
#         'total_price': total_price # NEW: Add the calculated total price to the context
#     }
#     return render(request, 'myapp/cart_detail.html', context) # NEW: Render the new cart_detail.html template with the context
# # --- END NEW: Cart Detail View ---



######################### ChapterXIV topic 15.5 The Satchel's Refinement: Modifying Cart Contents ######################

# myapp/views.py (updated with update_cart_item and remove_from_cart views)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json
# import uuid

# # Home view (retained)
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view (retained)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration (retained, with added messages)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.')
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login (retained, with added messages)
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout (retained, with added message)
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('product_list')

# # User Profile View (retained)
# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View (retained)
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = 'myapp/profile_edit.html'
#     success_url = reverse_lazy('profile_view')

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form)
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form
#             context['form'] = profile_form
#             return self.render_to_response(context)

# # Order History View (retained)
# class OrderHistoryView(LoginRequiredMixin, ListView):
#     model = Order
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created']

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View (retained)
# class VendorDashboardView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products'

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.all().order_by('-created')

# # Product List View (retained)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)

#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price)
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")

#         if max_price:
#             try:
#                 max_price = Decimal(max_price)
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')

#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '')
#         context['max_price'] = self.request.GET.get('max_price', '')

#         return context

# # Product Detail View (retained)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self):
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# # Add to Cart View (retained from 15.2)
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     cart = None
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 cart = None
#         if not cart:
#             cart = Cart.objects.create(user=None)
#             request.session['cart_id'] = str(cart.id)
#             messages.info(request, "A new anonymous cart was created for your session.")

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price}
#     )

#     if not created:
#         cart_item.quantity += quantity
#         cart_item.price = product.price
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     return redirect(product.get_absolute_url())

# # Cart Detail View (retained from 15.3)
# def cart_detail(request):
#     cart = None
#     if request.user.is_authenticated:
#         try:
#             cart = Cart.objects.get(user=request.user)
#         except Cart.DoesNotExist:
#             pass
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 pass

#     if not cart:
#         cart_items = []
#         total_price = Decimal('0.00')
#     else:
#         cart_items = cart.items.all()
#         total_price = cart.get_total_price()

#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'myapp/cart_detail.html', context)

# # --- NEW: Update Cart Item View ---
# def update_cart_item(request, item_id): # NEW function definition
#     if request.method == 'POST': # NEW: Only process POST requests
#         cart_item = get_object_or_404(CartItem, id=item_id) # NEW: Get the specific CartItem

#         # Identify the correct cart (retained logic from add_to_cart/cart_detail)
#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         # NEW: Check if the cart item belongs to the current user's cart
#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to modify this cart item.")
#             return redirect('cart_detail')

#         try:
#             quantity = int(request.POST.get('quantity')) # NEW: Get the new quantity from POST data
#             if quantity <= 0: # NEW: Handle invalid quantity (0 or negative)
#                 cart_item.delete() # NEW: Delete item if quantity is 0 or less
#                 messages.info(request, f"'{cart_item.product.name}' removed from your cart.")
#             else:
#                 cart_item.quantity = quantity # NEW: Update the quantity
#                 cart_item.save() # NEW: Save the updated cart item
#                 messages.success(request, f"Quantity of '{cart_item.product.name}' updated to {quantity}.")
#         except ValueError: # NEW: Handle non-numeric quantity input
#             messages.error(request, "Invalid quantity entered.")
#         except Exception as e: # NEW: Catch other potential errors
#             messages.error(request, f"An error occurred: {e}")

#     return redirect('cart_detail') # NEW: Redirect back to the cart detail page

# # --- END NEW: Update Cart Item View ---

# # --- NEW: Remove From Cart View ---

# def remove_from_cart(request, item_id): 
#     if request.method == 'POST': 
#         cart_item = get_object_or_404(CartItem, id=item_id) 

#         # Identify the correct cart (retained logic from add_to_cart/cart_detail)
#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         # NEW: Check if the cart item belongs to the current user's cart
#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to remove this cart item.")
#             return redirect('cart_detail')

#         try:
#             cart_item.delete() 
#             messages.success(request, 
#                     f"'{cart_item.product.name}' has been removed from your cart.")
#         except Exception as e: 
#             messages.error(request, f"An error occurred while removing item: {e}")

#     return redirect('cart_detail') 

# # --- END NEW: Remove From Cart View ---




######################### ChapterXIV topic 15.5: The Final Incantation: Implementing Checkout ######################


# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required # RETAINED
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json
# import uuid

# # Home view (retained)
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view (retained)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration (retained, with added messages)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.')
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login (retained, with added messages)
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout (retained, with added message)
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('product_list')

# # User Profile View (retained)
# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View (retained)
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = 'myapp/profile_edit.html'
#     success_url = reverse_lazy('profile_view')

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form)
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form
#             context['form'] = profile_form
#             return self.render_to_response(context)

# # Order History View (retained)
# class OrderHistoryView(LoginRequiredMixin, ListView):
#     model = Order
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created']

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View (retained)
# class VendorDashboardView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products'

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.all().order_by('-created')

# # Product List View (retained)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)

#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price)
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")
            
#         if max_price:
#             try:
#                 max_price = Decimal(max_price)
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')
        
#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '')
#         context['max_price'] = self.request.GET.get('max_price', '')
        
#         return context

# # Product Detail View (retained)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self):
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# # Add to Cart View (retained from 15.2)
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     cart = None
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 # If an anonymous cart is found and the user logs in, associate it
#                 # if request.user.is_authenticated: # This logic would go in a login view or middleware
#                 #     cart.user = request.user
#                 #     cart.save()
#                 #     del request.session['cart_id']
#             except Cart.DoesNotExist:
#                 pass

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price}
#     )

#     if not created:
#         cart_item.quantity += quantity
#         cart_item.price = product.price
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     return redirect(product.get_absolute_url())

# # Cart Detail View (retained from 15.3)
# def cart_detail(request):
#     cart = None
#     if request.user.is_authenticated:
#         try:
#             cart = Cart.objects.get(user=request.user)
#             # if cart is anonymous and user logs in, associate it
#             # if request.user.is_authenticated and cart.user is None:
#             #     cart.user = request.user
#             #     cart.save()
#             #     if 'cart_id' in request.session:
#             #         del request.session['cart_id']
#         except Cart.DoesNotExist:
#             pass
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 pass

#     if not cart:
#         cart_items = []
#         total_price = Decimal('0.00')
#     else:
#         cart_items = cart.items.all()
#         total_price = cart.get_total_price()

#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'myapp/cart_detail.html', context)

# # Update Cart Item View (retained from 15.4)
# def update_cart_item(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to modify this cart item.")
#             return redirect('cart_detail')

#         try:
#             quantity = int(request.POST.get('quantity'))
#             if quantity <= 0:
#                 cart_item.delete()
#                 messages.info(request, f"'{cart_item.product.name}' removed from your cart.")
#             else:
#                 cart_item.quantity = quantity
#                 cart_item.save()
#                 messages.success(request, f"Quantity of '{cart_item.product.name}' updated to {quantity}.")
#         except ValueError:
#             messages.error(request, "Invalid quantity entered.")
#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")

#     return redirect('cart_detail')

# # Remove From Cart View (retained from 15.4)
# def remove_from_cart(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to remove this cart item.")
#             return redirect('cart_detail')

#         try:
#             cart_item.delete()
#             messages.success(request, f"'{cart_item.product.name}' has been removed from your cart.")
#         except Exception as e:
#             messages.error(request, f"An error occurred while removing item: {e}")

#     return redirect('cart_detail')

# # --- NEW: Checkout View ---
# @login_required # NEW: Ensures only logged-in users can checkout
# def checkout(request): # NEW function definition for the checkout process
#     user_cart = get_object_or_404(Cart, user=request.user) # NEW: Get the authenticated user's cart
#     cart_items = user_cart.items.all() # NEW: Get all items in the user's cart

#     if not cart_items: # NEW: Prevent checkout if cart is empty
#         messages.warning(request, "Your cart is empty. Please add items before checking out.")
#         return redirect('product_list') # NEW: Redirect to product list if cart is empty

#     if request.method == 'POST': # NEW: Process form submission
#         # In a real application, you would process payment here
#         # For now, we'll simulate order creation
#         try:
#             # Create a new Order
#             order = Order.objects.create( # NEW: Create a new Order object
#                 user=request.user,
#                 total_price=user_cart.get_total_price(), # NEW: Use cart's total price
#                 # You would add shipping address fields here from a form
#                 # e.g., shipping_address_line1=request.POST.get('address1'),
#                 # shipping_city=request.POST.get('city'), etc.
#             )

#             # Move cart items to order items
#             for item in cart_items: # NEW loop: Iterate through cart items
#                 OrderItem.objects.create( # NEW: Create an OrderItem for each CartItem
#                     order=order,
#                     product=item.product,
#                     quantity=item.quantity,
#                     price=item.price # Use the price at the time of adding to cart
#                 )
#                 # Optionally, reduce product stock here
#                 # item.product.stock -= item.quantity
#                 # item.product.save()

#             user_cart.items.all().delete() # NEW: Clear the cart after order creation
#             messages.success(request, f"Your order #{order.id} has been placed successfully!")
#             return redirect('order_confirmation', order_id=order.id) # NEW: Redirect to order confirmation page

#         except Exception as e: # NEW: General error handling for order processing
#             messages.error(request, f"There was an error processing your order: {e}")
#             return redirect('cart_detail') # NEW: Redirect back to cart on error

#     # For GET request, simply display the checkout page (with cart summary)
#     context = { # NEW: Prepare context for GET request
#         'cart': user_cart,
#         'cart_items': cart_items,
#         'total_price': user_cart.get_total_price(),
#         # You might pass a form for shipping details here in the future
#     }
#     return render(request, 'myapp/checkout.html', context) # NEW: Render the checkout template

# # --- END NEW: Checkout View ---

# # --- NEW: Order Confirmation View ---
# @login_required # NEW: Ensures only logged-in users can view their orders
# def order_confirmation(request, order_id): # NEW function definition for order confirmation
#     order = get_object_or_404(Order, id=order_id, user=request.user) # NEW: Get the specific order for the user
#     order_items = order.items.all() # NEW: Get all items in the order

#     context = { # NEW: Create context for the template
#         'order': order,
#         'order_items': order_items,
#     }
#     return render(request, 'myapp/order_confirmation.html', context) # NEW: Render the order confirmation template
# # --- END NEW: Order Confirmation View ---




######################### ChapterXVIII Section 18.3: The Client-Side Charm: Conjuring Payment Elements ######################


# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required # RETAINED
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json
# import uuid

# from django.shortcuts import render
# from django.conf import settings # Import settings to access STRIPE_PUBLISHABLE_KEY

# # Home view (retained)
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view (retained)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration (retained, with added messages)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.')
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login (retained, with added messages)
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout (retained, with added message)
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('product_list')

# # User Profile View (retained)
# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View (retained)
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = 'myapp/profile_edit.html'
#     success_url = reverse_lazy('profile_view')

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form)
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form
#             context['form'] = profile_form
#             return self.render_to_response(context)

# # Order History View (retained)
# class OrderHistoryView(LoginRequiredMixin, ListView):
#     model = Order
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created']

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View (retained)
# class VendorDashboardView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products'

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.all().order_by('-created')

# # Product List View (retained)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)

#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price)
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")
            
#         if max_price:
#             try:
#                 max_price = Decimal(max_price)
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')
        
#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '')
#         context['max_price'] = self.request.GET.get('max_price', '')
        
#         return context

# # Product Detail View (retained)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self):
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# # Add to Cart View (retained from 15.2)
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     cart = None
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 # If an anonymous cart is found and the user logs in, associate it
#                 # if request.user.is_authenticated: # This logic would go in a login view or middleware
#                 #     cart.user = request.user
#                 #     cart.save()
#                 #     del request.session['cart_id']
#             except Cart.DoesNotExist:
#                 pass

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price}
#     )

#     if not created:
#         cart_item.quantity += quantity
#         cart_item.price = product.price
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     return redirect(product.get_absolute_url())

# # Cart Detail View (retained from 15.3)
# def cart_detail(request):
#     cart = None
#     if request.user.is_authenticated:
#         try:
#             cart = Cart.objects.get(user=request.user)
#             # if cart is anonymous and user logs in, associate it
#             # if request.user.is_authenticated and cart.user is None:
#             #     cart.user = request.user
#             #     cart.save()
#             #     if 'cart_id' in request.session:
#             #         del request.session['cart_id']
#         except Cart.DoesNotExist:
#             pass
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 pass

#     if not cart:
#         cart_items = []
#         total_price = Decimal('0.00')
#     else:
#         cart_items = cart.items.all()
#         total_price = cart.get_total_price()

#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'myapp/cart_detail.html', context)

# # Update Cart Item View (retained from 15.4)
# def update_cart_item(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to modify this cart item.")
#             return redirect('cart_detail')

#         try:
#             quantity = int(request.POST.get('quantity'))
#             if quantity <= 0:
#                 cart_item.delete()
#                 messages.info(request, f"'{cart_item.product.name}' removed from your cart.")
#             else:
#                 cart_item.quantity = quantity
#                 cart_item.save()
#                 messages.success(request, f"Quantity of '{cart_item.product.name}' updated to {quantity}.")
#         except ValueError:
#             messages.error(request, "Invalid quantity entered.")
#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")

#     return redirect('cart_detail')

# # Remove From Cart View (retained from 15.4)
# def remove_from_cart(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to remove this cart item.")
#             return redirect('cart_detail')

#         try:
#             cart_item.delete()
#             messages.success(request, f"'{cart_item.product.name}' has been removed from your cart.")
#         except Exception as e:
#             messages.error(request, f"An error occurred while removing item: {e}")

#     return redirect('cart_detail')

# # --- NEW: Checkout View ---
# @login_required # NEW: Ensures only logged-in users can checkout
# def checkout(request): # NEW function definition for the checkout process
#     user_cart = get_object_or_404(Cart, user=request.user) # NEW: Get the authenticated user's cart
#     cart_items = user_cart.items.all() # NEW: Get all items in the user's cart

#     if not cart_items: # NEW: Prevent checkout if cart is empty
#         messages.warning(request, "Your cart is empty. Please add items before checking out.")
#         return redirect('product_list') # NEW: Redirect to product list if cart is empty

#     if request.method == 'POST': # NEW: Process form submission
#         # In a real application, you would process payment here
#         # For now, we'll simulate order creation
#         try:
#             # Create a new Order
#             order = Order.objects.create( # NEW: Create a new Order object
#                 user=request.user,
#                 total_price=user_cart.get_total_price(), # NEW: Use cart's total price
#                 # You would add shipping address fields here from a form
#                 # e.g., shipping_address_line1=request.POST.get('address1'),
#                 # shipping_city=request.POST.get('city'), etc.
#             )

#             # Move cart items to order items
#             for item in cart_items: # NEW loop: Iterate through cart items
#                 OrderItem.objects.create( # NEW: Create an OrderItem for each CartItem
#                     order=order,
#                     product=item.product,
#                     quantity=item.quantity,
#                     price=item.price # Use the price at the time of adding to cart
#                 )
#                 # Optionally, reduce product stock here
#                 # item.product.stock -= item.quantity
#                 # item.product.save()

#             user_cart.items.all().delete() # NEW: Clear the cart after order creation
#             messages.success(request, f"Your order #{order.id} has been placed successfully!")
#             return redirect('order_confirmation', order_id=order.id) # NEW: Redirect to order confirmation page

#         except Exception as e: # NEW: General error handling for order processing
#             messages.error(request, f"There was an error processing your order: {e}")
#             return redirect('cart_detail') # NEW: Redirect back to cart on error

#     # For GET request, simply display the checkout page (with cart summary)
#     context = { # NEW: Prepare context for GET request
#         'cart': user_cart,
#         'cart_items': cart_items,
#         'total_price': user_cart.get_total_price(),
#         # You might pass a form for shipping details here in the future
#     }
#     return render(request, 'myapp/checkout.html', context) # NEW: Render the checkout template

# # --- END NEW: Checkout View ---

# # --- NEW: Order Confirmation View ---
# @login_required # NEW: Ensures only logged-in users can view their orders
# def order_confirmation(request, order_id): # NEW function definition for order confirmation
#     order = get_object_or_404(Order, id=order_id, user=request.user) # NEW: Get the specific order for the user
#     order_items = order.items.all() # NEW: Get all items in the order

#     context = { # NEW: Create context for the template
#         'order': order,
#         'order_items': order_items,
#     }
#     return render(request, 'myapp/order_confirmation.html', context) # NEW: Render the order confirmation template
# # --- END NEW: Order Confirmation View ---



# def checkout_view(request):
#     # Pass the Stripe Publishable Key to the template
#     context = {
#         'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
#     }
#     return render(request, 'myapp/checkout_view.html', context)




######################### ChapterXVIII Section Section 18.4: The Server-Side Ledger: Processing Charges with Django #################


# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView, View, UpdateView
# from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
# from django.db.models import Q
# from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib import messages
# from django.urls import reverse_lazy
# from decimal import Decimal
# import json
# import uuid
# from django.conf import settings

# # NEW IMPORTS for Payment Processing

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt 
# import stripe 


# # Home view (retained)
# def home_view(request):
#     return render(request, 'myapp/home.html')

# # Contact view (retained)
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             print(f"New contact message from {name} ({email}): {message}")
#             return redirect('product_list')
#         else:
#             pass
#     else:
#         form = ContactForm()
#     return render(request, 'myapp/contact.html', {'form': form})

# # User Registration (retained, with added messages)
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             messages.success(request, f'Account created for {user.username}! You can now log in.')
#             return redirect('product_list')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = UserCreationForm()
#     return render(request, 'myapp/register.html', {'form': form})

# # User Login (retained, with added messages)
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('product_list')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'myapp/login.html', {'form': form})

# # User Logout (retained, with added message)
# def user_logout(request):
#     auth_logout(request)
#     messages.info(request, "You have been logged out.")
#     return redirect('product_list')

# # User Profile View (retained)
# class UserProfileView(LoginRequiredMixin, DetailView):
#     model = UserProfile
#     template_name = 'myapp/profile.html'
#     context_object_name = 'user_profile'

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

# # User Profile Update View (retained)
# class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = 'myapp/profile_edit.html'
#     success_url = reverse_lazy('profile_view')

#     def get_object(self):
#         return get_object_or_404(UserProfile, user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserUpdateForm(instance=self.request.user)
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = self.get_form()

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return self.form_valid(profile_form)
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             context = self.get_context_data()
#             context['user_form'] = user_form
#             context['form'] = profile_form
#             return self.render_to_response(context)

# # Order History View (retained)
# class OrderHistoryView(LoginRequiredMixin, ListView):
#     model = Order
#     template_name = 'myapp/order_history.html'
#     context_object_name = 'orders'
#     ordering = ['-created']

#     def get_queryset(self):
#         return Order.objects.filter(user=self.request.user)

# # Vendor Dashboard View (retained)
# class VendorDashboardView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'myapp/vendor_dashboard.html'
#     context_object_name = 'products'

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_staff:
#             messages.error(request, "You are not authorized to view the vendor dashboard.")
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return Product.objects.all().order_by('-created')

# # Product List View (retained)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'myapp/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6

#     def get_queryset(self):
#         queryset = Product.objects.filter(available=True)

#         query = self.request.GET.get('q')
#         if query:
#             queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

#         category_slug = self.request.GET.get('category')
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)

#         min_price = self.request.GET.get('min_price')
#         max_price = self.request.GET.get('max_price')

#         if min_price:
#             try:
#                 min_price = Decimal(min_price)
#                 queryset = queryset.filter(price__gte=min_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid minimum price entered.")

#         if max_price:
#             try:
#                 max_price = Decimal(max_price)
#                 queryset = queryset.filter(price__lte=max_price)
#             except ValueError:
#                 messages.error(self.request, "Invalid maximum price entered.")

#         return queryset.order_by('name')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all().order_by('name')

#         context['selected_category_slug'] = self.request.GET.get('category', '')
#         context['current_query'] = self.request.GET.get('q', '')
#         context['min_price'] = self.request.GET.get('min_price', '')
#         context['max_price'] = self.request.GET.get('max_price', '')

#         return context

# # Product Detail View (retained)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'myapp/product_detail.html'
#     context_object_name = 'product'

#     def get_object(self):
#         return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# # Add to Cart View (retained from 15.2)
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     try:
#         quantity = int(request.POST.get('quantity', 1))
#         if quantity <= 0:
#             messages.error(request, "Quantity must be a positive number.")
#             return redirect(product.get_absolute_url())
#     except ValueError:
#         messages.error(request, "Invalid quantity entered.")
#         return redirect(product.get_absolute_url())

#     cart = None
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         if created:
#             messages.info(request, "A new cart was created for your account.")
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 # If an anonymous cart is found and the user logs in, associate it
#                 # if request.user.is_authenticated: # This logic would go in a login view or middleware
#                 #     cart.user = request.user
#                 #     cart.save()
#                 #     del request.session['cart_id']
#             except Cart.DoesNotExist:
#                 pass

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart,
#         product=product,
#         defaults={'quantity': quantity, 'price': product.price}
#     )

#     if not created:
#         cart_item.quantity += quantity
#         cart_item.price = product.price
#         cart_item.save()
#         messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
#     else:
#         messages.success(request, f"'{product.name}' added to your cart.")
#     return redirect(product.get_absolute_url())

# # Cart Detail View (retained from 15.3)
# def cart_detail(request):
#     cart = None
#     if request.user.is_authenticated:
#         try:
#             cart = Cart.objects.get(user=request.user)
#             # if cart is anonymous and user logs in, associate it
#             # if request.user.is_authenticated and cart.user is None:
#             #     cart.user = request.user
#             #     cart.save()
#             #     if 'cart_id' in request.session:
#             #         del request.session['cart_id']
#         except Cart.DoesNotExist:
#             pass
#     else:
#         session_cart_id = request.session.get('cart_id')
#         if session_cart_id:
#             try:
#                 cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#             except Cart.DoesNotExist:
#                 pass

#     if not cart:
#         cart_items = []
#         total_price = Decimal('0.00')
#     else:
#         cart_items = cart.items.all()
#         total_price = cart.get_total_price()

#     context = {
#         'cart': cart,
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'myapp/cart_detail.html', context)

# # Update Cart Item View (retained from 15.4)
# def update_cart_item(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to modify this cart item.")
#             return redirect('cart_detail')

#         try:
#             quantity = int(request.POST.get('quantity'))
#             if quantity <= 0:
#                 cart_item.delete()
#                 messages.info(request, f"'{cart_item.product.name}' removed from your cart.")
#             else:
#                 cart_item.quantity = quantity
#                 cart_item.save()
#                 messages.success(request, f"Quantity of '{cart_item.product.name}' updated to {quantity}.")
#         except ValueError:
#             messages.error(request, "Invalid quantity entered.")
#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")

#     return redirect('cart_detail')

# # Remove From Cart View (retained from 15.4)
# def remove_from_cart(request, item_id):
#     if request.method == 'POST':
#         cart_item = get_object_or_404(CartItem, id=item_id)

#         cart = None
#         if request.user.is_authenticated:
#             try:
#                 cart = Cart.objects.get(user=request.user)
#             except Cart.DoesNotExist:
#                 pass
#         else:
#             session_cart_id = request.session.get('cart_id')
#             if session_cart_id:
#                 try:
#                     cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
#                 except Cart.DoesNotExist:
#                     pass

#         if not cart or cart_item.cart != cart:
#             messages.error(request, "You are not authorized to remove this cart item.")
#             return redirect('cart_detail')

#         try:
#             cart_item.delete()
#             messages.success(request, f"'{cart_item.product.name}' has been removed from your cart.")
#         except Exception as e:
#             messages.error(request, f"An error occurred while removing item: {e}")

#     return redirect('cart_detail')

# # --- NEW: Checkout View (from 15.5) ---
# @login_required
# def checkout(request):
#     user_cart = get_object_or_404(Cart, user=request.user)
#     cart_items = user_cart.items.all()

#     if not cart_items:
#         messages.warning(request, "Your cart is empty. Please add items before checking out.")
#         return redirect('product_list')

#     if request.method == 'POST':
#         # This is where the order is created.
#         # We will integrate payment processing here or link to it.
#         try:
#             order = Order.objects.create(
#                 user=request.user,
#                 total_price=user_cart.get_total_price(),
#             )

#             for item in cart_items:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item.product,
#                     quantity=item.quantity,
#                     price=item.price
#                 )
#             user_cart.items.all().delete()
#             messages.success(request, f"Your order #{order.id} has been placed successfully!")
#             return redirect('order_confirmation', order_id=order.id)

#         except Exception as e:
#             messages.error(request, f"There was an error processing your order: {e}")
#             return redirect('cart_detail')

#     context = {
#         'cart': user_cart,
#         'cart_items': cart_items,
#         'total_price': user_cart.get_total_price(),
#     }
#     return render(request, 'myapp/checkout.html', context) # This template is for order summary/shipping details

# # --- END NEW: Checkout View ---

# # --- NEW: Order Confirmation View (from 15.5) ---
# @login_required
# def order_confirmation(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     order_items = order.items.all()

#     context = {
#         'order': order,
#         'order_items': order_items,
#     }
#     return render(request, 'myapp/order_confirmation.html', context)
# # --- END NEW: Order Confirmation View ---


# # NEW: Checkout View for Stripe Form (renders the HTML page with Stripe Elements)
# @login_required
# def stripe_payment_form_view(request):
#     # Pass the Stripe Publishable Key to the template
#     context = {
#         'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
#     }
#     return render(request, 'myapp/checkout_view.html', context) # Using checkout_view.html

# # NEW: Payment processing view (receives token from client-side, processes charge)


# @csrf_exempt 
# def process_payment(request):
#     if request.method == 'POST':
#         try:            
#             data = json.loads(request.body)
#             token_id = data.get('token')
#             amount = data.get('amount') 

#             if not token_id or not amount:
#                 return JsonResponse({'success': False, 
#                                      'error': 'Missing token or amount'}, status=400)
         
#             charge = stripe.Charge.create(
#                 amount=amount,          
#                 currency='usd',         
#                 source=token_id,       
#                 description='Example charge for e-commerce item',                
#             )
            
#             if charge.status == 'succeeded':              
#                 print(f"Stripe Charge successful: {charge.id}")
#                 return JsonResponse({'success': True, 
#                                      'message': 'Payment successful!'})
#             else:
#                 print(f"Stripe Charge failed: {charge.status}")
#                 return JsonResponse({'success': False, 'error': 'Payment failed',
#                                      'status': charge.status}, status=400)

#         except stripe.error.CardError as e:            
#             body = e.json_body
#             err = body.get('error', {})
#             print(f"Stripe Card Error: {err.get('message')}")
#             return JsonResponse({'success': False, 
#                                  'error': err.get('message')}, status=400)
#         except stripe.error.StripeError as e:           
#             print(f"Stripe Error: {e}")
#             return JsonResponse({'success': False, 'error': str(e)}, status=500)
#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 
#                                  'error': 'Invalid JSON in request body'}, status=400)
#         except Exception as e:            
#             print(f"Unexpected error: {e}")
#             return JsonResponse({'success': False, 
#                                  'error': 'An unexpected error occurred.'}, status=500)
#     else:
#         return JsonResponse({'success': False, 
#                              'error': 'Invalid request method'}, status=405)




######################### ChapterXVIII Section 18.5: The Unified Checkout #################

# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import Product, Category, UserProfile, Order, OrderItem, Cart, CartItem
from django.db.models import Q
from .forms import ContactForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from decimal import Decimal
import json
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
import stripe 


# Home view (retained)
def home_view(request):
    return render(request, 'myapp/home.html')

# Contact view (retained)
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"New contact message from {name} ({email}): {message}")
            return redirect('product_list')
        else:
            pass
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

# User Registration (retained, with added messages)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('product_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

# User Login (retained, with added messages)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

# User Logout (retained, with added message)
def user_logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('product_list')

# User Profile View (retained)
class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'myapp/profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

# User Profile Update View (retained)
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'myapp/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = self.get_form()

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return self.form_valid(profile_form)
        else:
            messages.error(request, 'Please correct the errors below.')
            context = self.get_context_data()
            context['user_form'] = user_form
            context['form'] = profile_form
            return self.render_to_response(context)

# Order History View (retained)
class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'myapp/order_history.html'
    context_object_name = 'orders'
    ordering = ['-created']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

# Vendor Dashboard View (retained)
class VendorDashboardView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'myapp/vendor_dashboard.html'
    context_object_name = 'products'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "You are not authorized to view the vendor dashboard.")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Product.objects.all().order_by('-created')

# Product List View (retained)
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            try:
                min_price = Decimal(min_price)
                queryset = queryset.filter(price__gte=min_price)
            except ValueError:
                messages.error(self.request, "Invalid minimum price entered.")
            
        if max_price:
            try:
                max_price = Decimal(max_price)
                queryset = queryset.filter(price__lte=max_price)
            except ValueError:
                messages.error(self.request, "Invalid maximum price entered.")

        return queryset.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        
        context['selected_category_slug'] = self.request.GET.get('category', '')
        context['current_query'] = self.request.GET.get('q', '')
        context['min_price'] = self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('max_price', '')
        
        return context

# Product Detail View (retained)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_detail.html'
    context_object_name = 'product'

    def get_object(self):
        return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'])

# Add to Cart View (retained from 15.2)
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            messages.error(request, "Quantity must be a positive number.")
            return redirect(product.get_absolute_url())
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect(product.get_absolute_url())

    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        if created:
            messages.info(request, "A new cart was created for your account.")
    else:
        session_cart_id = request.session.get('cart_id')
        if session_cart_id:
            try:
                cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
                # If an anonymous cart is found and the user logs in, associate it
                # if request.user.is_authenticated: # This logic would go in a login view or middleware
                #     cart.user = request.user
                #     cart.save()
                #     del request.session['cart_id']
            except Cart.DoesNotExist:
                pass

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity, 'price': product.price}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.price = product.price
        cart_item.save()
        messages.success(request, f"Added {quantity} more of '{product.name}' to your cart. Total: {cart_item.quantity}.")
    else:
        messages.success(request, f"'{product.name}' added to your cart.")
    return redirect(product.get_absolute_url())

# Cart Detail View (retained from 15.3)
def cart_detail(request):
    cart = None
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            # if cart is anonymous and user logs in, associate it
            # if request.user.is_authenticated and cart.user is None:
            #     cart.user = request.user
            #     cart.save()
            #     if 'cart_id' in request.session:
            #         del request.session['cart_id']
        except Cart.DoesNotExist:
            pass
    else:
        session_cart_id = request.session.get('cart_id')
        if session_cart_id:
            try:
                cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
            except Cart.DoesNotExist:
                pass

    if not cart:
        cart_items = []
        total_price = Decimal('0.00')
    else:
        cart_items = cart.items.all()
        total_price = cart.get_total_price()

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'myapp/cart_detail.html', context)

# Update Cart Item View (retained from 15.4)
def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)

        cart = None
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                pass
        else:
            session_cart_id = request.session.get('cart_id')
            if session_cart_id:
                try:
                    cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
                except Cart.DoesNotExist:
                    pass

        if not cart or cart_item.cart != cart:
            messages.error(request, "You are not authorized to modify this cart item.")
            return redirect('cart_detail')

        try:
            quantity = int(request.POST.get('quantity'))
            if quantity <= 0:
                cart_item.delete()
                messages.info(request, f"'{cart_item.product.name}' removed from your cart.")
            else:
                cart_item.quantity = quantity
                cart_item.save()
                messages.success(request, f"Quantity of '{cart_item.product.name}' updated to {quantity}.")
        except ValueError:
            messages.error(request, "Invalid quantity entered.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return redirect('cart_detail')

# Remove From Cart View (retained from 15.4)
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)

        cart = None
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                pass
        else:
            session_cart_id = request.session.get('cart_id')
            if session_cart_id:
                try:
                    cart = Cart.objects.get(id=session_cart_id, user__isnull=True)
                except Cart.DoesNotExist:
                    pass

        if not cart or cart_item.cart != cart:
            messages.error(request, "You are not authorized to remove this cart item.")
            return redirect('cart_detail')

        try:
            cart_item.delete()
            messages.success(request, f"'{cart_item.product.name}' has been removed from your cart.")
        except Exception as e:
            messages.error(request, f"An error occurred while removing item: {e}")

    return redirect('cart_detail')

# --- UPDATED: Checkout View (from 15.5, now also handles Stripe form rendering) ---
@login_required
def checkout(request):
    user_cart = get_object_or_404(Cart, user=request.user)
    cart_items = user_cart.items.all()

    if not cart_items:
        messages.warning(request, "Your cart is empty. Please add items before checking out.")
        return redirect('product_list')

    # For GET request, display the checkout page with cart summary and Stripe form
    context = {
        'cart': user_cart,
        'cart_items': cart_items,
        'total_price': user_cart.get_total_price(),
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY, # Pass key to template
    }
    # The POST logic for this 'checkout' view (order creation) will now be handled
    # by the 'process_payment' view after a successful Stripe charge.
    # So, we remove the direct POST handling from here.
    return render(request, 'myapp/checkout.html', context)

# --- END UPDATED: Checkout View ---

# --- NEW: Order Confirmation View (from 15.5) ---
@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()

    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'myapp/order_confirmation.html', context)
# --- END NEW: Order Confirmation View ---


# REMOVED: The 'stripe_payment_form_view' is no longer needed as its functionality
# is now integrated directly into the 'checkout' view that renders checkout.html.
# This function was previously named 'checkout_view' in earlier instructions.
# @login_required
# def stripe_payment_form_view(request):
#     context = {
#         'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
#     }
#     return render(request, 'myapp/checkout_view.html', context)



# UPDATED: Payment processing view (receives token from client-side, processes charge, creates order, clears cart)
@csrf_exempt # WARNING: For tutorial simplicity. In production, use proper CSRF protection.
@login_required # Ensure user is logged in to process payment for their cart
def process_payment(request):
    if request.method == 'POST':
        # Get the authenticated user's cart
        try:
            user_cart = Cart.objects.get(user=request.user)
            cart_items = user_cart.items.all()
            if not cart_items:
                return JsonResponse({'success': False, 'error': 'Your cart is empty.'}, status=400)
            
            total_amount_decimal = user_cart.get_total_price()
            # Stripe amount must be an integer in cents
            # Convert Decimal to int, handling potential floating point issues if necessary
            # Multiply by 100 to convert dollars to cents
            amount_in_cents = int(total_amount_decimal * 100)

        except Cart.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No active cart found for this user.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': f'Failed to retrieve cart details: {e}'}, status=500)


        try:
            # Parse the incoming JSON data from the client
            data = json.loads(request.body)
            token_id = data.get('token')
            # IMPORTANT: We are now using the 'amount_in_cents' calculated from the server-side cart
            # to prevent client-side tampering with the price. The 'amount' from client is ignored for charge.

            if not token_id:
                return JsonResponse({'success': False, 'error': 'Missing payment token.'}, status=400)

            # Create a Stripe Charge
            # For simplicity, we'll use Charge here. PaymentIntent is recommended for production.
            charge = stripe.Charge.create(
                amount=amount_in_cents, # Use amount calculated from server's cart
                currency='usd',         # Currency (e.g., 'usd', 'eur')
                source=token_id,        # The token representing the payment method
                description=f'Order #{user_cart.id} for {request.user.username}',
                metadata={'order_id': user_cart.id, 'user_id': request.user.id},
            )

            # Check if the charge was successful
            if charge.status == 'succeeded':
                # --- NEW PRINT STATEMENT ADDED HERE ---
                print(f"Stripe Charge successful: {charge.id}")
                # --- END NEW PRINT STATEMENT ---

                # Create a new Order based on the cart
                order = Order.objects.create(
                    user=request.user,
                    total_price=total_amount_decimal, # Use the Decimal total price
                    # You might add payment_id=charge.id, status='paid' etc. to your Order model
                    # For now, we'll assume default status and link to charge via metadata if needed.
                )

                # Move cart items to order items
                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.price # Use the price at the time of adding to cart
                    )
                    # Optionally, reduce product stock here:
                    # item.product.stock -= item.quantity
                    # item.product.save()

                user_cart.items.all().delete() # Clear the cart after order creation
                messages.success(request, f"Your order #{order.id} has been placed and paid successfully!")
                
                # Return success with the order ID for client-side redirection
                return JsonResponse({'success': True, 'message': 'Payment successful!', 'order_id': order.id})
            else:
                print(f"Stripe Charge failed: {charge.status}")
                return JsonResponse({'success': False, 'error': 'Payment failed', 'status': charge.status}, status=400)

        except stripe.error.CardError as e:
            # Card was declined
            body = e.json_body
            err = body.get('error', {})
            error_message = err.get('message', 'Your card was declined.')
            print(f"Stripe Card Error: {error_message}")
            return JsonResponse({'success': False, 'error': error_message}, status=400)
        except stripe.error.StripeError as e:
            # Other Stripe errors (e.g., network, API errors)
            print(f"Stripe Error: {e}")
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON in request body'}, status=400)
        except Exception as e:
            # Catch any other unexpected errors
            print(f"Unexpected error in process_payment: {e}")
            return JsonResponse({'success': False, 'error': 'An unexpected error occurred during payment processing.'}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

