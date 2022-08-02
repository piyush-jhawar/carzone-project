from django.urls import path

from cars import views

urlpatterns = [
    path("", view=views.cars, name="cars"),
    path("<int:id>/", view=views.car_detail, name='car_detail'),

]
