from django import forms
from django.shortcuts import get_object_or_404
from airport.models import Airport
from .models import Review


class ReviewCreateForm(forms.ModelForm):
    """
    レビュー作成フォーム
    """
    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            if data['airport']:
                obj = get_object_or_404(Airport, name_ja=data['airport'])
                data['airport'] = obj.id
        super(ReviewCreateForm, self).__init__(data=data, *args, **kwargs)

    class Meta:
        model = Review
        fields = (
            'airport',
            'rate_synthesis',
            'review_title',
            'review_text',
        )
        # widgets = {
        #     'rate_clean': forms.TextInput(),
        # }