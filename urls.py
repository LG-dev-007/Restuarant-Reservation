from django import urls
from django.urls import path
from .import views


urlpatterns = [
    
    path("<int:id>", views.index, name="index"),
    path("homepage/", views.homepage, name="homepage"),
    path("reserve/", views.reserve, name="reserve"),
    path("register/", views.register, name="register"),
    path("login_user/", views.loginpage, name="login_user"),
    path("payment/", views.paymentmodule, name="payment"),
    path("confirmation/", views.confirmation, name="conformation"),
    
]
