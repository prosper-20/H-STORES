from django.urls import path
from .views import home, register2, register, login2, logout, profile
from django.contrib.auth import views as auth_views

# This part is for the email activation flow
from .views import (
    SignUpView,
    ActivateView,
    CheckEmailView,
    SuccessView,
    MyPasswordResetView
)


urlpatterns = [
    path("", home, name="home"),
    path("register2/", register2, name="register2"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("login/", login2, name="login"),
    path("logout/", logout, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('success/', SuccessView.as_view(), name="success"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]