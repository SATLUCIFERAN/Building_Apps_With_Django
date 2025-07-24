


################## Chapter XI  topic 11.6 Django Forms: The Alchemist's Form-Building Spells ##############

# from django import forms

# class ContactForm(forms.Form):
#     """
#     A simple contact form for customer inquiries.
#     """
#     name = forms.CharField(max_length=100, label="Your Name")   
#     email = forms.EmailField(label="Your Email")   
#     message = forms.CharField(widget=forms.Textarea, label="Your Message")





############################# Chapter XI topics 11.8 Implementing reCAPTCHA: Integrating the Humanity Test ################


# from django import forms
# from django_recaptcha.fields import ReCaptchaField     # <--- ADD THIS IMPORT!
# from django_recaptcha.widgets import ReCaptchaV2Checkbox # <--- ADD THIS IMPORT!

# class ContactForm(forms.Form):
#     """
#     A simple contact form for customer inquiries.
#     """
#     name = forms.CharField(max_length=100, label="Your Name")   
#     email = forms.EmailField(label="Your Email")   
#     message = forms.CharField(widget=forms.Textarea, label="Your Message")

#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 




############################# Chapter XII topics12.18 Crafting the Profile Editing Forms: The Customer's Quill ################


from django import forms
from django_recaptcha.fields import ReCaptchaField     
from django_recaptcha.widgets import ReCaptchaV2Checkbox 
from .models import Product, Category, UserProfile # <--- ADD THIS IMPORT!
from django.contrib.auth.models import User # <--- ADD THIS IMPORT!

class ContactForm(forms.Form):
    """
    A simple contact form for customer inquiries.
    """
    name = forms.CharField(max_length=100, label="Your Name")   
    email = forms.EmailField(label="Your Email")   
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'country', 'profile_picture']
