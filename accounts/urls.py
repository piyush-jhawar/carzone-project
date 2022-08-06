from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", view=views.login, name="login"),
    path("register/", view=views.register, name="register"),
    path("logout/", view=views.logout, name="logout"),
    path("dashboard/", view=views.dashboard, name="dashboard"),
]
