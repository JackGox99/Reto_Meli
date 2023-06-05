from django.apps import AppConfig

# Se realiza el mapeo de la API


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
