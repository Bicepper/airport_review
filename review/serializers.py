from rest_framework import serializers

from .models import Review


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            'id',
            'rate_synthesis',
            'review_date',
            'review_update',
            'review_title',
            'review_text',
            'review_img_01',
        )