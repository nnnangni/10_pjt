from rest_framework import serializers
from .models import Genre, Movie, Score

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# class MovieDetailSerializers(serializers.ModelSerializer):
#     # movies = MovieSerializers(source="movie_set", many=True)
#     class Meta:
#         model = Movie
#         fields = '__all__'

# 장고에 있는 데이터베이스를 json으로 바꿔줌
class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','name']
        
class GenreDetailSerializers(serializers.ModelSerializer):
    movies = MovieSerializers(source="movie_set", many=True)
    class Meta:
        model = Genre
        fields = ['id','name','movies']
        
class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id','content','value']