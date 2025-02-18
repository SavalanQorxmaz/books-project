from django.urls import path
from apis.views import BookListCreateAPIView, BookDetailsAPIView, BookDetailsWithSlugAPIView

app_name = "apis"

urlpatterns = [
    path(
        "books/",
        BookListCreateAPIView.as_view(),
        name="books"
    ),

    path(
        "books/<int:book_id>/",
        BookDetailsAPIView.as_view(),
        name="book-details"
    ),

    path(
        "books/<slug:slug>/",
        BookDetailsWithSlugAPIView.as_view(),
        name="book-details-with-slug"
    )

]