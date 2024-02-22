from django.urls import path
from ebooks.api.views import (
    EbookListCreateAPIView,
    EbookDetailsAPIView,
    ReviewDetailAPIView,
    ReviewCreateAPIView,
)

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>/", EbookDetailsAPIView.as_view(), name="ebook-details"),
    path("ebooks/<int:ebook_pk>/reviews/", ReviewCreateAPIView.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetailAPIView.as_view(), name="review-details"),
]
