from calendar import c
from cgitb import lookup
from rest_framework.decorators import api_view
from rest_framework.response import Response # типо render
from . import serializers
from . import models
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class DirectorListAPIView(APIView):
    def get(self, request):
        directors = models.Director.objects.all()
        data = serializers.DirectorSerializers(directors, many=True).data
        return Response(data=data)


    def post(self, request):
        serializer = serializers.CreateUpdateDirectors(data = request.data)
        if not serializer.is_valid():
            return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        directors = models.Director.objects.create(name = name)
        return Response(data = serializers.DirectorSerializers(directors).data, status = status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def DirectorListView(request):
#     if request.method == 'GET':
#         directors = models.Director.objects.all()
#         data = serializers.DirectorSerializers(directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.CreateUpdateDirectors(data = request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         name = request.data.get('name')
#         directors = models.Director.objects.create(name = name)
#         return Response(data = serializers.DirectorSerializers(directors).data, status = status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.CreateUpdateDirectors
    lookup_field = 'id'





# @api_view(['GET', 'DELETE', 'PUT'])
# def DirectorDetailView(request, id):
#     try:    
#         director = models.Director.objects.get(id = id)
#     except models.Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
#     if request.method == 'GET':
#         data = serializers.DirectorSerializers(director).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = serializers.CreateUpdateDirectors(data = request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data=serializers.DirectorSerializers(director).data)


class MovieListAPIView(APIView):
    def get(self, request):
        movie = models.Movie.objects.all()
        data = serializers.MovieSerializersList(movie, many=True).data
        return Response(data=data)


    def post(self, request):
        serializer = serializers.CreateUpdateMovies(data = request.data)
        if not serializer.is_valid():
            return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = models.Movie.objects.create(title = title, description = description, duration = duration, director_id= director_id)
        return Response(data=serializers.MovieSerializersList(movie).data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'POST'])
# def MovieListView(request):
#     if request.method == 'GET':
#         movie = models.Movie.objects.all()
#         data = serializers.MovieSerializersList(movie, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.CreateUpdateMovies(data = request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director_id = request.data.get('director_id')
#         movie = models.Movie.objects.create(title = title, description = description, duration = duration, director_id= director_id)
#         return Response(data=serializers.MovieSerializersList(movie).data, status=status.HTTP_201_CREATED)


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.CreateUpdateMovies
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def MovieDetailView(request, id):
#     try:
#         movie = models.Movie.objects.get(id = id)
#     except models.Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found'})
#     if request.method == 'GET':
#         data = serializers.MovieSerializersDetail(movie).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = serializers.CreateUpdateMovies(data = request.data)
#         if not serializer.is_valid():
#             return Response(data={'errors':serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data= serializers.MovieSerializersDetail(movie).data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status.HTTP_204_NO_CONTENT)



class ReviewListAPIView(APIView):
    def get(self, request):
        review = models.Review.objects.all()
        data = serializers.ReviewSerializers(review, many=True).data
        return Response(data=data)

    
    def post(self, request):
        serializer = serializers.CreateUpdateReviews(data = request.data)
        if not serializer.is_valid():
            return Response(data = {"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = models.Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(serializers.ReviewSerializers(review).data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def ReviewListView(request):
#     if request.method == 'GET':
#         review = models.Review.objects.all()
#         data = serializers.ReviewSerializers(review, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = serializers.CreateUpdateReviews(data = request.data)
#         if not serializer.is_valid():
#             return Response(data = {"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         text = request.data.get('text')
#         movie_id = request.data.get('movie_id')
#         stars = request.data.get('stars')
#         review = models.Review.objects.create(text=text, movie_id=movie_id, stars=stars)
#         return Response(serializers.ReviewSerializers(review).data, status=status.HTTP_201_CREATED)


class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.CreateUpdateReviews
    lookup_field = 'id'

# @api_view(['GET', 'DELETE', 'PUT'])
# def ReviewDetailView(request, id):
#     try:
#         review = models.Review.objects.get(id = id)
#     except models.Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Review not found'})
#     if request.method == 'GET':
#         data = serializers.ReviewSerializers(review).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = serializers.CreateUpdateReviews(data = request.data)
#         if not serializer.is_valid():
#             return Response(data = {"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
#         review.text = request.data.get('text')
#         review.movie_id = request.data.get('movie_id')
#         review.stars = request.data.get('stars')
#         review.save()
#         return Response(data = serializers.ReviewSerializers(review).data)


class MovieReviesListAPIView(APIView):
    def get(self, request):
        movie = models.Movie.objects.all()
        data = serializers.MoviesSerializersList(movie, many=True).data
        return Response(data=data)

# @api_view(['GET'])
# def MoviesReviesList(request):
#     movie = models.Movie.objects.all()
#     data = serializers.MoviesSerializersList(movie, many=True).data
#     return Response(data=data)


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class Authorization(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(data={"error": "user not found!"}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def authorization(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     user = authenticate(username=username, password=password)
#     if user:
#         Token.objects.filter(user=user).delete()
#         token = Token.objects.create(user=user)
#         return Response(data={'key': token.key})
#     return Response(data={"error": "user not found!"}, status=status.HTTP_404_NOT_FOUND)


from django.contrib.auth.models import User
from django.core.mail import send_mail

class Registration(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        model = User.objects.create_user(username=username, password=password, email=email)
        return Response(data= {'message': 'User created'}, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def registration(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     email = request.data.get("email")
#     model = User.objects.create_user(username=username, password=password, email=email)
#     return Response(data= {'message': 'User created'}, status=status.HTTP_201_CREATED)


