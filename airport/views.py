from django.shortcuts import render
from airport.models import Airport

from django.views import generic


def list(request):
    return render(request, 'airport/index.html')


class Detail(generic.DetailView):
    model = Airport
    template_name = 'airport/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['id'] = timezone.now()
        return context
