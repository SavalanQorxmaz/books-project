from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer



class BooksAPIView(generics.ListAPIView):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
        

class BookDetailsAPIView(generics.GenericAPIView):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=kwargs.get('book_id'))
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    