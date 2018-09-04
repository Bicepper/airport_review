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
from airport.views import list

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('signup/done/', UserCreateDone.as_view(), name='create_done'),
    path('signup/complete/<token>/', UserCreateComplete.as_view(), name='create_complete'),
    path('airport/', list, name='airport'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='reset/password_reset.html',
        email_template_name='reset/password_reset_email.html',
        subject_template_name='reset/password_reset_subject.txt'
    ), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'
    ), name='password_reset_complete'),
]