from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

# ---------------------------------------------------------------------------------------------
# Function Based API VIEW :

# decorators: is a function that takes another function as argument and adds funtionality or augments  the function without changing it.
#            In below example @api_view is decorator which converts function based view into APIView subclass

'''

@api_view(['GET', 'POST'])
def artile_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
    elif request.method == "PUT":

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''


# ---------------------------------------------------------------------------------------
# Class Based API VIEW: Litte More Advantages over Function Based API VIEW. DRY, Reusability, 


'''
class ArticleList(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    


class ArticleDetails(APIView):
     
    def get_object(self, id):
        try: 
            return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''


# ----------------------------------------------------------------------------------------------
# Generic View: Shortcut for View development. used for quickly build APIView.



#------------------------------------------------------------------------------------------------
# APIView: allow us to define funtions that match standard HTTP methods like GET,POST,PUT,PATCH,etc.
# Viewsets: allow us to funtions that match to common API object actions like, LIST, CREATE, RETRIVE,UPDATE etc.

# viewsets and APIView: CRUD operation only xa vaney, directly viewsets use garni to respect DRY principle.
# otherwise go on low level. i.e. apiview. Afterall viewsets are also subclass of APIView.

# Generic api view: this class extends REST Framework's APIVIEW class, adding commonly required behaviour
# for standard list and detail views.

# ==================================================================================================
# ModelViewset

class ArticleViewset(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class ArticleDetails(viewsets.ModelViewSet):
    
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    

    
