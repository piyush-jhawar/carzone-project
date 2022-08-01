from django.urls import path

from cars import views

urlpatterns = [
    path("", view=views.cars, name="cars"),

]
