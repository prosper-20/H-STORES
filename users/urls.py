from django.urls import path
from .views import home, register2, register, login2, logout
from django.contrib.auth import views as auth_views

# This part is for the email activation flow
from .views import (
    SignUpView,
    ActivateView,
    CheckEmailView,
    SuccessView,
)


urlpatterns = [
    path("", home, name="home"),
    path("register2/", register2, name="register2"),
    path("register/", register, name="register"),
    path("login/", login2, name="login"),
    path("logout/", logout, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('success/', SuccessView.as_view(), name="success"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]