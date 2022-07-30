from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from pages import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path('about/', view=views.about, name='about'),
    path('services/', view=views.services, name='services'),
    path('contact/', view=views.contact, name='contact'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)