from rest_framework import serializers

from .models import Review
from users.models import User
from users.serializers import UserSerializers


class ReviewRuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'lounge_id',
        )


class ReviewSerializers(serializers.ModelSerializer):
    rate_synthesis = serializers.SerializerMethodField()
    dialog = serializers.SerializerMethodField()
    review_img_01 = serializers.SerializerMethodField()
    user = UserSerializers(many=True, read_only=True)
    review_date = serializers.DateTimeField(format='%Y年%m月%d日', read_only=True)
    review_update = serializers.DateTimeField(format='%Y年%m月%d日', read_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'rate_synthesis',
            'review_date',
            'review_update',
            'review_title',
            'review_text',
            'dialog',
            'review_img_01',
            'user',
            'lounge_id',
        )

    def get_rate_synthesis(self, obj):
        cast_int = int(obj.rate_synthesis)
        return cast_int

    def get_dialog(self, obj):
        dialog = False
        return dialog

    def get_review_img_01(self, obj):
        before_check = obj.review_img_01
        if before_check == '':
            return ""
        else:
            return "/{a}".format(a=obj.review_img_01.url)

    def to_representation(self, instance):
        representation = super(ReviewSerializers, self).to_representation(instance)
        imglist = []
        if str(instance.review_img_01) != '':
            imglist.append("/{a}".format(a=str(instance.review_img_01)))
        representation.update({
            'imglist': imglist,
            'imglen': len(imglist),
        })
        return representation

    # def get_userinfo(self, obj):
    #     try:
    #         print('=======================')
    #         xxx = Review.objects.user.all().get(id=obj.id)
    #         print(xxx)
    #         print('=======================')
    #         user_abstruct = UserSerializers(User.objects.get(id=Review.objects.get(id=obj.id).id)).data
    #         return user_abstruct
    #     except():
    #         user_abstruct = None
    #         return user_abstruct
