from rest_framework import serializers

from .models import Review
from users.models import User
from users.serializers import UserSerializers


class ReviewSerializers(serializers.ModelSerializer):
    # user = serializers.RelatedField(read_only=True)
    userinfo = serializers.SerializerMethodField()

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
            'userinfo',
        )

    def get_userinfo(self, obj):
        try:
            user_abstruct = UserSerializers(User.objects.get(id=Review.objects.get(id=obj.id).id)).data
            return user_abstruct
        except():
            user_abstruct = None
            return user_abstruct
