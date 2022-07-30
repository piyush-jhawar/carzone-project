from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request=request, template_name="pages/home.html", context={})


def about(request):
    return render(request=request, template_name="pages/about.html", context={})


def services(request):
    return render(request=request, template_name="pages/services.html", context={})

def contact(request):
    return render(request=request, template_name="pages/contact.html", context={})