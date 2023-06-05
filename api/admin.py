from django.contrib import admin
from .models import Users

# Se realiza el registro del modelo Users para ser visto desde la consola de administración

admin.site.register(Users)
