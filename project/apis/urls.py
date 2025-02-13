from django.urls import path
from apis.views import BooksAPIView, BookDetailsAPIView

app_name = "apis"

urlpatterns = [
    path(
        "books/",
        BooksAPIView.as_view(),
        name="books"
    ),

    path(
        "books/<int:book_id>/",
        BookDetailsAPIView.as_view(),
        name="book-details"
    )
]