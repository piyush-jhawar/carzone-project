from django.urls import path

from contacts import views

urlpatterns = [
    path("inquiry/", view=views.inquiry, name="inquiry"),
]
