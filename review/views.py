from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect

from .models import Review

from .forms import (
    ReviewCreateForm,
)

User = get_user_model()


class NewReview(generic.CreateView):
    """
    レビュー作成
    """
    model = Review
    template_name = 'account/user_detail.html'
    form_class = ReviewCreateForm

    # def form_valid(self, form):
    #     obj = form.save()
    #     obj.user.add(self.request.user)
    #     obj.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        obj = form.save(commit=False)
        try:
            userreviewed = Review.objects.filter(user=self.request.user)
            print('=================ここから開始=================')
            for a in userreviewed:
                if obj.airport_id == a.airport_id:
                    raise ValueError('既にレビュー済みです。')
            print('=================ここまで終了=================')
            obj.save()
            obj.user.add(self.request.user)
            obj.save()
            return HttpResponseRedirect(self.get_success_url())
        except Review.DoesNotExist:
            pass

        # obj = form.save(commit=False)
        # obj.user = get_object_or_404(Review, user=self.request.user, airport_id=obj.airport_id)
        # print(obj.user)
        # obj.form.save()
        # obj.user.add(self.request.user)
        # obj.save()
        # return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return resolve_url('account_review_list', pk=self.kwargs['pk'])


class ListReview(generic.ListView):
    """
    レビュー一覧
    """
    model = Review
    paginate_by = 10
    template_name = 'account/user_detail.html'
