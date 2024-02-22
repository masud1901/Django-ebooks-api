from rest_framework import generics, mixins

from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer


class EbookListCreateAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)