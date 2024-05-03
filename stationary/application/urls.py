from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("items/", views.items, name="items"),
    path("buy", views.buy, name="buy"),
    path("sell/", views.sell, name="sell"),
    path("about/", views.about, name="about"),
    path("signin/", views.signin, name="signin"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("contact/", views.contact, name="contact"),
]
