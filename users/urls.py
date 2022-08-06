from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.riderReg, name="register"),
    path("customer/", views.customerReg, name="customer"),
    path("profile/", views.profile, name="profile"),
    path("loggedout/", views.logOut, name="loggedout")
]
