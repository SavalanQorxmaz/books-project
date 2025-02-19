from rest_framework import views, generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from utils.paginations import CustomCursorPagination

from books.models import Book
from books.serializers import BookSerializer, BookCreateSerializer



class BookListCreateAPIView(generics.GenericAPIView):
    queryset = Book.objects.all() 
    # pagination_class = CustomCursorPagination
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer  
        return BookSerializer  
    
    def get_queryset(self):
        return super().get_queryset()

    # def get(self, request, *args, **kwargs):
    #     books = self.paginate_queryset(self.get_queryset())
    #     serializer = self.get_serializer(books, many=True)
    #     return self.get_paginated_response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

class BookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "book_id"
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get(self.lookup_field))
    
    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class BookDetailsWithSlugAPIView(generics.GenericAPIView):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "slug"
    
    def get_object(self):
        return get_object_or_404(self.get_queryset(), slug=self.kwargs.get(self.lookup_field))
    
    def get(self, request, *args, **kwargs):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    