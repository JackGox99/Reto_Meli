from rest_framework import routers
from django.urls import path, include
from . import views

# Crea un enrutador de Django REST Framework
router = routers.DefaultRouter()

# Registra la vista UserViewSet en el enrutador con la ruta 'users'
router.register(r'users', views.UserViewSet, basename='CRUD Users')

urlpatterns = [
    # Tus otros patrones de URL
    # Incluye las URL registradas en el enrutador
    path('', include(router.urls)),
    # Ruta para escanear la base de datos
    path('database/scan/', views.IdColumns.as_view(), name='Database Scan'),
    path('database/scan/<int:column_id>/', views.GetColumnId.as_view(),
         name='scan'),  # Ruta para obtener un ID de columna específico
]
