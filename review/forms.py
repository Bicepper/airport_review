from django import forms

from airport.models import Airport
from .models import Review


class ReviewCreateForm(forms.ModelForm):
    """
    レビュー作成フォーム
    """
    class Meta:
        model = Review
        fields = (
            'airport',
            'rate_clean',
            'rate_facility',
            'rate_lounge',
            'rate_service',
            'rate_access',
            'review_title',
            'review_text',
        )
        widgets = {
            'airport': forms.TextInput,
            'rate_clean': forms.TextInput(attrs={'name':'rate_clean'}),
        }