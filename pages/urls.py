from django.urls import path

from pages import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path('about/', view=views.about, name='about'),
    path('services/', view=views.services, name='services'),
    path('contact/', view=views.contact, name='contact'),

]
