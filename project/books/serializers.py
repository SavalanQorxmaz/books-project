from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Book
        fields = [
            'id',
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
        
    # def create(self, validated_data):
    #     return super().create(validated_data)
    def create(self, validated_data):
        # Yalnız validated_data istifadə edin, id avtomatik təyin olunacaq.
        return Book.objects.create(**validated_data)