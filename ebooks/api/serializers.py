from rest_framework import serializers
from ebooks.models import Review, Ebook


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = [
            "ebook",
        ]
        # fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Ebook
        fields = "__all__"
