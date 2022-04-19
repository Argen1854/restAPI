from random import choice, choices
from django.forms import CharField
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from . import models


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = "id name movies_count".split()


class MovieSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "id title description duration director".split()

class MoviesSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = 'id title description duration director reviews_count rating_count'.split()

class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"


class CreateUpdateDirectors(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class CreateUpdateMovies(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=5)
    description = serializers.CharField(max_length=1000)
    duration = serializers.TimeField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            models.Director.objects.get(id=director_id)
        except:
            raise ValidationError(f"Director with id={director_id} not found!")
        return director_id


class CreateUpdateReviews(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    stars = serializers.IntegerField(min_value=1, max_value =5)
    movie_id = serializers.IntegerField()
    def validate_movie_id(self, movie_id):
        try:
            models.Movie.objects.get(id=movie_id)
        except:
            raise ValidationError(f"Movie with id={movie_id} not found!")
        return movie_id


