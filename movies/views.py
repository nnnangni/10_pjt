from django.shortcuts import render, get_object_or_404
from . models import Genre, Movie, Score
from .serializers import GenreSerializers, MovieSerializers, GenreDetailSerializers, ScoreSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializers(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_id):
    # genre = Genre.objects.get(id=genre_id)
    # 없는데이터 넣을때 예를들면 11개 데이터만 있는데 12번 넣으면?
    genre = get_object_or_404(Genre, id=genre_id)
    serializer = GenreDetailSerializers(genre)
    return Response(serializer.data)

@api_view(['GET'])  
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])  
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)
    
@api_view(['POST'])  
def score_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ScoreSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        # return Response(serializer.data)
        return Response({"message":"작성되었습니다"})
  
@api_view(['PUT','DELETE','GET'])       
def scores(request, score_id):
    score = get_object_or_404(Score, id=score_id)
    if request.method == "PUT":
        serializer = ScoreSerializers(data=request.data, instance=score)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"수정되었습니다."})
    elif request.method == "DELETE":
        score.delete()
        return Response({"message":"삭제되었습니다."})
    elif request.method == "GET":
        serializer = ScoreSerializers(score)
        return Response(serializer.data)