from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from .serilizer import UserSerializer
from .models import Users


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class IdColumns(APIView):
    def get(self, request):
        table_name = 'api_users'  # Replace with the actual table name

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT ordinal_position, column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'")
            column_ids = cursor.fetchall()

        column_id = {column[0]: column[1] for column in column_ids}

        return Response({'database_ids': column_id})


class GetColumnId(APIView):
    def get_field_type(self, column_id):
        if column_id is None:
            return None

        table_name = 'api_users'  # Replace with the actual table name

        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}' AND ordinal_position = {column_id}")
            result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

    def get(self, request, column_id):
        field_type = self.get_field_type(column_id)

        if field_type is not None:
            return Response({'column_id': column_id, 'field_type': field_type})
        else:
            return Response({'column_id': column_id, 'field_type': 'Field not found'})
