from rest_framework import serializers
from ebooks.models import Review, Ebook


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Ebook
        fields = "__all__"
