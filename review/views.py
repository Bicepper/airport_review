from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Review

from .forms import (
    ReviewCreateForm,
)

User = get_user_model()


class NewReview(generic.CreateView):
    """
    レビュー作成
    """
    template_name = 'account/user_detail.html'
    form_class = ReviewCreateForm

