from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts.users'
    label = 'accounts_users'
    verbose_name = 'Users' 