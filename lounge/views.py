from django.shortcuts import render
from lounge.models import Lounge
from review.models import Review

from django.views import generic
from rest_framework import generics
from review.serializers import ReviewRuleSerializers


def LoungeList(request):
    return render(request, 'lounge/index.html')


class LoungeDetail(generic.DetailView):
    model = Lounge
    template_name = 'lounge/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['object'] = self.object.pk  # レビュー画面で利用できるようにセッション格納
        return context


class LoungeDetailViewSet(generics.ListAPIView):
    serializer_class = ReviewRuleSerializers

    def get_queryset(self):
        query_my_name = self.kwargs['id']
        return Review.objects.filter(id=query_my_name)

