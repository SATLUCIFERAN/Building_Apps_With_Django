

################## Chapter XII part 12.16 Automatically Creating UserProfile for New Users: The Binding Spell ############


from django.db.models.signals import post_save # <--- NEW: Import the post_save signal
from django.contrib.auth.models import User # <--- NEW: Import the User model
from django.dispatch import receiver # <--- NEW: Import the receiver decorator
from .models import UserProfile # <--- NEW: Import your UserProfile model

@receiver(post_save, sender=User) # <--- Decorator to register this function as a signal receiver
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to automatically create a UserProfile when a new User is created.
    This function is called by Django's signal system.
    """
   
    if created: # Check if a new User instance was just created (not updated)       
        UserProfile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to automatically save the UserProfile when the User is saved (for updates).
    This ensures that if the User object is updated, its related UserProfile is also saved.
    """
    instance.userprofile.save()
