# from django.db.models.signals import post_save # <--- NEW: Import the post_save signal
# from django.contrib.auth.models import User # <--- NEW: Import the User model
# from django.dispatch import receiver # <--- NEW: Import the receiver decorator
# from .models import UserProfile # <--- NEW: Import your UserProfile model

# @receiver(post_save, sender=User) # <--- Decorator to register this function as a signal receiver
# def create_user_profile(sender, instance, created, **kwargs):
#     """
#     Signal receiver to automatically create a UserProfile when a new User is created.
#     This function is called by Django's signal system.
#     """
#     # Detailed Explanation: This function acts as the "receiver" for the post_save signal.
#     # `sender`: The model class that sent the signal (in this case, the User model).
#     # `instance`: The actual instance of the model that was just saved (the User object).
#     # `created`: A boolean argument. It is `True` if a new record was just created in the database,
#     #            and `False` if an existing record was updated. This is crucial for our logic.
#     # `**kwargs`: Catches any additional keyword arguments that might be sent with the signal.
#     # Logic & Imagination: This is the Binding Spell. It listens intently for a new page
#     # being added to the Register (a new User object being saved).
#     if created: # Check if a new User instance was just created (not updated)
#         # Detailed Explanation: This conditional ensures that a UserProfile is created
#         # *only* when a new User object is first saved to the database (i.e., during registration),
#         # not every time an existing user's data is updated.
#         UserProfile.objects.create(user=instance)
#         # Detailed Explanation: If `created` is True, this line creates a new UserProfile instance.
#         # It sets the `user` field of the new UserProfile to the `instance` (the newly created User object),
#         # establishing the One-to-One link.
#         # Logic & Imagination: If it's a new page in the Register, the spell immediately conjures a new,
#         # blank personalized scroll and magically binds it to that new page, ensuring every new customer
#         # has their own unique record from the very beginning.

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     """
#     Signal receiver to automatically save the UserProfile when the User is saved (for updates).
#     This ensures that if the User object is updated, its related UserProfile is also saved.
#     """
#     # Detailed Explanation: This second receiver handles updates. When a User object is saved (even if not created),
#     # we want to ensure its associated UserProfile is also saved. This is important if you later add logic
#     # to the UserProfile's save method (like our image resizing) that needs to run on updates.
#     # `instance.userprofile.save()`: Accesses the related UserProfile object through the `userprofile` attribute
#     # (which Django automatically adds to the User model due to the OneToOneField) and calls its save method.
#     # Logic & Imagination: This part of the Binding Spell ensures that if the main page of the Register is updated
#     # (e.g., email changed), its associated personalized scroll is also refreshed or saved, ensuring consistency.
#     instance.userprofile.save()





############################################### Deploy ###############################################################

# myapp/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile # Import your UserProfile model

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to automatically create a UserProfile when a new User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # else:
    #    # This 'else' block is often used to handle updates for existing profiles.
    #    # However, for simplicity and to avoid potential infinite loops with save(),
    #    # we'll rely on explicit profile updates or the profile.save() in the template/form.
    #    # If you have specific logic in UserProfile.save() that needs to run on User updates,
    #    # you might need to reconsider this, but for now, this is safer.
    #    # instance.userprofile.save() # Removed from here to prevent infinite recursion

# MODIFIED: Ensure profile exists before attempting to save it
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver to automatically save the UserProfile when the User is saved (for updates).
    Ensures that if the User object is updated, its related UserProfile is also saved,
    but only if the profile already exists.
    """
    try:
        # Attempt to save the profile if it exists
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        # If the profile does not exist, it means this user was created
        # before the signal was fully active, or there was an issue.
        # We can optionally log this or handle it, but for now,
        # we just prevent a crash. The create_user_profile should
        # handle new users going forward.
        pass # Do nothing if profile doesn't exist; it will be created on next user creation