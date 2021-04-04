from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Django doc recommend doing this way to avoid side effect of import
    def ready(self):
    	import users.signals
