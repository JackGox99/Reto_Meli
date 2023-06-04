from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='CRUD Users')

urlpatterns = [
    # Your other URL patterns
    path('', include(router.urls)),
    path('database/scan/',
         views.IdColumns.as_view(), name='Database Scan'),
    path('database/scan/<int:column_id>/',
         views.GetColumnId.as_view(), name='scan'),
]
