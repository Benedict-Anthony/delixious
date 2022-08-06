from django.urls import path
from . import views

app_name="store"
urlpatterns = [
    path("", views.index, name="home"),
    path("menu", views.menu, name="menu"),
    path("checkout", views.checkout, name="checkout"),
    path("success", views.sucess, name="success",),
    path("check-out-sessions/<int:id>", views.check_out_session, name="check-out-sessions"),
    path("update-cart/", views.update_cart, name="update-cart")
]
