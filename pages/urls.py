from django.urls import path

from pages import views

urlpatterns = [
    path("", view=views.home, name="home"),
    
]