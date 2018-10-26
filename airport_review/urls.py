"""airport_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path
from django.urls import include
from top.views import index
from users.views import UserCreate
from users.views import UserCreateDone
from users.views import UserCreateComplete
from users.views import PasswordReset
from users.views import PasswordResetDone
from users.views import PasswordResetConfirm
from users.views import PasswordResetComplete
from airport.views import list
from airport.views import Detail
from account.views import AccountUpdateEmail
from account.views import AccountUpdateIntro
from account.views import AccountUpdateSocialmedia
from review.views import NewReview
from review.views import ListReview

from country.api_urls import country_router
from alliance.api_urls import alliance_router
from airline.api_urls import airline_router
from airport.api_urls import airport_router

api_urlpatterns = [
    path('countries/', include(country_router.urls)),
    path('alliances/', include(alliance_router.urls)),
    path('airlines/', include(airline_router.urls)),
    path('airports/', include(airport_router.urls)),
]

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('api/1.0/', include(api_urlpatterns)),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('signup/done/', UserCreateDone.as_view(), name='create_done'),
    path('signup/complete/<token>/', UserCreateComplete.as_view(), name='create_complete'),
    path('airport/', list, name='airport'),
    path('airport/<int:pk>/', Detail.as_view(), name='airport_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('reset/', PasswordReset.as_view(), name='password_reset'),
    path('reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    # path('account/<int:pk>/', Account.as_view(), name='account'),
    # path('account_update/<int:pk>/', AccountUpdate.as_view(), name='account_update'),
    path('account/<slug:pk>/email', AccountUpdateEmail.as_view(), name='account_update_email'),
    path('account/<int:pk>/intro', AccountUpdateIntro.as_view(), name='account_update_intro'),
    path('account/<int:pk>/sns', AccountUpdateSocialmedia.as_view(), name='account_update_sns'),
    path('account/<int:pk>/new_review', NewReview.as_view(), name='account_review_new'),
    path('account/<int:pk>/list_review', ListReview.as_view(), name='account_review_list'),
]