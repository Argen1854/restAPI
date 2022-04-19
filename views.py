from calendar import c
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from products.models import Review
from products.serializers import ReviewSerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView



class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    pagination_class = PageNumberPagination
    filter_fields = ['product']

    

class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = "id"
    

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class RegisterAPIView(APIView):
    serializer = serializers.UserCreateSerializers
    def post(self, request):
        serializer = self.serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get("username")
        password = request.data.get("password")
        User.objects.create_user(username = username, password=password) # create_user = для создвние пользователя и create_superuser для админа
        return Response(data= {'message': 'User created'}, status=status.HTTP_201_CREATED)


