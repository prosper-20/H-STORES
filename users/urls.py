from django.urls import path
from .views import home, register2, register, login, logout

urlpatterns = [
    path("", home, name="home"),
    path("register2/", register2, name="register2"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout")
]