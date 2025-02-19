from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'description',
            'slug'
        ]
        

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'slug'
        ]
    
        
class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description'
        ]
        
    def create(self, validated_data):
        return super().create(validated_data)