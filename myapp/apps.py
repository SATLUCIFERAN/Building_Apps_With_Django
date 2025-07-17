
# from django.apps import AppConfig


# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'



###################### Chapter XII part 5 topics12.16 import signals #######################

from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self): # <--- NEW: Override the ready method
        # Detailed Explanation: The `ready` method is called by Django when your application
        # is fully loaded and configured. This is the ideal place to import your signals module,
        # as it ensures that all models are loaded and ready before your signal handlers are
        # connected.
        import myapp.signals # <--- NEW: Import your signals module
        # Detailed Explanation: By importing `myapp.signals` here, all the `@receiver` decorators
        # within that module are processed, and your `create_user_profile` and `save_user_profile`
        # functions are successfully connected to the `post_save` signal of the User model.
        # Logic & Imagination: When your magical application chamber is fully
        # prepared and ready for operation, you activate the Binding Spell
        # (import myapp.signals) so it can begin listening for new identities
        # being added to the Register.