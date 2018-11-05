from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from django.shortcuts import resolve_url
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Review
from airport.models import Airport
from lounge.models import Lounge

from .forms import (
    ReviewCreateForm,
)

User = get_user_model()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        """
        現在ログインしているユーザーのPKと、表示しているマイページのPIDが同一か判定
        スーパーユーザーは無条件で表示
        """
        print("============ユーザー情報の確認：開始==========")
        print(self.request.user.pid.hex)
        print("============ユーザー情報の確認：終了==========-")
        user = self.request.user
        return user.pid.hex == self.kwargs['pid'] or user.is_superuser


class NewReview(OnlyYouMixin, generic.CreateView):
    """
    レビュー作成
    """
    model = Review
    # template_name = 'account/user_review.html'
    template_name = 'lounge/review_new.html'
    form_class = ReviewCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'lounge_detail': Lounge.objects.get(id=self.request.session['object']),
        })
        # context['lounge_detail'] = Lounge.objects.get(id=self.request.session['object'])
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.lounge_id = self.request.session['object']
        try:
            userreviewed = Review.objects.filter(user=self.request.user)
            for a in userreviewed:
                if obj.lounge_id == a.lounge_id:
                    raise ValueError('既にレビュー済みです。')
            obj.upload_to_userid(self.request.user.id)
            obj.save()
            obj.user.add(self.request.user)
            # print('============kusakusa=====--')
            # print(self.request.user.id)
            # print('============kusakusa=====--')

            obj.save()
            return HttpResponseRedirect(self.get_success_url())
        except Review.DoesNotExist:
            pass

    def form_invalid(self, form):
        print('invalid通ってる！')
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return resolve_url('lounge_detail', pk=self.kwargs['pk'])


class ListReview(generic.ListView):
    """
    レビュー一覧
    """
    model = Review
    paginate_by = 10
    template_name = 'account/user_detail.html'
