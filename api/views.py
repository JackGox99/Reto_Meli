from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from .serilizer import UserSerializer
from .models import Users


# Create your views here.

# Definición de la vista UserViewSet como un ModelViewSet de Django REST Framework
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

# Vista IdColumns que escanea la base de datos y devuelve los identificadores de columna


class IdColumns(APIView):
    def get(self, request):
        table_name = 'api_users'  # Reemplazar con el nombre real de la tabla

        with connection.cursor() as cursor:
            # Ejecuta una consulta SQL para obtener los identificadores, nombres y tipos de columna
            cursor.execute(
                f"SELECT ordinal_position, column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
            column_ids = cursor.fetchall()

        # Crea un diccionario con los identificadores de columna como clave y los nombres de columna como valor
        column_id = {column[0]: column[1] for column in column_ids}

        return Response({'database_ids': column_ids})

# Vista GetColumnId que obtiene el tipo de campo para un identificador de columna específico


class GetColumnId(APIView):
    def get_field_type(self, column_id):
        if column_id is None:
            return None

        table_name = 'api_users'  # Reemplazar con el nombre real de la tabla

        with connection.cursor() as cursor:
            # Ejecuta una consulta SQL para obtener el nombre y tipo de campo para el identificador de columna dado
            cursor.execute(
                f"SELECT column_name, data_type, data_type FROM information_schema.columns WHERE table_name = '{table_name}' AND ordinal_position = {column_id}")
            result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

    def get(self, request, column_id):
        # Obtiene el tipo de campo para el identificador de columna dado
        field_type = self.get_field_type(column_id)

        if field_type is not None:
            return Response({'column_id': column_id, 'field_type': field_type})
        else:
            return Response({'column_id': column_id, 'field_type': 'Field not found'})
