
from django import forms

class ContactForm(forms.Form):
    """
    A simple contact form for customer inquiries.
    """
    name = forms.CharField(max_length=100, label="Your Name")
    # Logic & Imagination: This declares a text field for the customer's name.
    # Django will expect up to 100 characters and display "Your Name" as its label.

    email = forms.EmailField(label="Your Email")
    # Logic & Imagination: This declares an email field. Django will automatically
    # validate that the input looks like a valid email address (e.g., contains '@' and '.').

    message = forms.CharField(widget=forms.Textarea, label="Your Message")
    # Logic & Imagination: This declares a multi-line text area for the message.
    # The 'widget=forms.Textarea' explicitly tells Django to render this as an
    # HTML <textarea> element, not a single-line input.

    # You can add a CAPTCHA field here later if needed (as discussed in Part 3)




########################### Chaptere XI part 3  updated for reCAPTCHA  ######################################

# from django import forms
# from django_recaptcha.fields import ReCaptchaField     # <--- ADD THIS IMPORT!
# from django_recaptcha.widgets import ReCaptchaV2Checkbox # <--- ADD THIS IMPORT!

# class ContactForm(forms.Form):
#     """
#     A simple contact form for customer inquiries, now with CAPTCHA protection.
#     """
#     name = forms.CharField(
#         max_length=100,
#         label="Your Name",
#         widget=forms.TextInput(attrs={'class': 'form-control rounded-md shadow-sm'})
#     )

#     email = forms.EmailField(
#         label="Your Email",
#         widget=forms.EmailInput(attrs={'class': 'form-control rounded-md shadow-sm'})
#     )

#     message = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control rounded-md shadow-sm', 'rows': 5}),
#         label="Your Message"
#     )

#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 



######################### Chapter XII Part 6 topic 12.18  Crafting the Profile Editing Forms: ###########################

from django import forms
from .models import Product, Category, UserProfile # <-- Import UserProfile
from django.contrib.auth.models import User # <-- Import Django's User model
from django_recaptcha.fields import ReCaptchaField     # <--- ADD THIS IMPORT!
from django_recaptcha.widgets import ReCaptchaV2Checkbox # <--- ADD THIS IMPORT!

# ... (ContactForm as before) ...

class ContactForm(forms.Form):
   
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={'class': 'form-control rounded-md shadow-sm'})
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={'class': 'form-control rounded-md shadow-sm'})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control rounded-md shadow-sm', 'rows': 5}),
        label="Your Message"
    )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 



class UserUpdateForm(forms.ModelForm):
    """
    Form for updating basic User model fields.
    """
    email = forms.EmailField() # Make email field explicit for validation and display
    # Logic & Imagination: This form is a small, specialized quill for updating
    # the customer's core identity details on their main Register page.

    class Meta:
        model = User # This form is based on the User model
        fields = ['username', 'first_name', 'last_name', 'email'] # Fields allowed for editing
        # Detailed Explanation:
        # `model = User`: Tells Django that this form is directly linked to the User model.
        # `fields = [...]`: Specifies which fields from the User model should be included in this form.
        #   - 'username': Allows users to change their username.
        #   - 'first_name', 'last_name': Standard fields for personal names.
        #   - 'email': We explicitly define it above as `forms.EmailField()` to ensure proper email validation
        #     and display, even though it's also in the `User` model. This is good practice.

class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating UserProfile model fields, including profile picture.
    """
    # Logic & Imagination: This form is the main, versatile quill for updating
    # all the unique details on the customer's personalized scroll.

    class Meta:
        model = UserProfile # This form is based on the UserProfile model
        fields = ['phone_number', 'address', 'city', 'country', 'profile_picture'] # Fields allowed for editing
        # Detailed Explanation:
        # `model = UserProfile`: Links this form to our custom UserProfile model.
        # `fields = [...]`: Lists all the custom fields we want the user to be able to edit.
        #   - 'profile_picture': Django's ImageField automatically renders as a file input.
        #     When a file is uploaded, Django handles the saving to MEDIA_ROOT and our
        #     `UserProfile.save()` method will handle the resizing.
