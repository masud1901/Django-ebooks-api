from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer
from ebooks.api.permissions import IsAdminUserOrReadOnly,IsReviewAuthorOrReadOnly

# class EbookListCreateAPIView(
#     generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
# ):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError(
                {"review_author": ["You have already written a review for this ebook."]}
            )

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]
 