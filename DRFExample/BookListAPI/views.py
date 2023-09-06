from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET','POST'])
def books(request):
    return Response('List of books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if (author):
            return Response({'message':f'list of books by {author}'}, status=status.HTTP_200_OK)
        return Response({'message':'list of books'}, status=status.HTTP_200_OK)
    
    def post(self, request):
        title = request.data.get('title')
        if title:
            return Response({'title':title}, status=status.HTTP_201_CREATED)
        return Response({'message':'new book created'}, status=status.HTTP_201_CREATED)
    
class BookView(APIView):
    def get(self, request, pk):
        return Response({'message':f'single book with id {pk}'}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        title = request.data.get('title')
        if title:
            return Response({'id':pk,'title':title}, status=status.HTTP_201_CREATED)
        return Response({'message':f'new book created by id {pk}'}, status=status.HTTP_201_CREATED)
    