# from django.apps import AppConfig


# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'



################## Chapter XII part 12.16 Automatically Creating UserProfile for New Users: The Binding Spell ############

from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        
        import myapp.signals
