from rest_framework import generics, mixins

from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer


class EbookList(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    pass
