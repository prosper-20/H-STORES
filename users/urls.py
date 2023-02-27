from django.urls import path
from .views import home, register2, register, login, logout


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
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('success/', SuccessView.as_view(), name="success"),
]