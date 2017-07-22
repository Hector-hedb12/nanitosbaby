from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'nanitosbaby.users'
    verbose_name = "Usuario"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
