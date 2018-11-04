from django.shortcuts import render
from lounge.models import Lounge

from django.views import generic


def LoungeList(request):
    return render(request, 'lounge/index.html')


class LoungeDetail(generic.DeleteView):
    model = Lounge
    template_name = 'lounge/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
