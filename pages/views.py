from django.shortcuts import render

from pages.models import Team, Social

# Create your views here.


def home(request):
    if request.method == "GET":
        teams = Team.objects.all()
        return render(request=request, template_name="pages/home.html", context={"teams": teams})
    elif request.method == "POST":
        pass


def about(request):
    if request.method == "GET":
        teams = Team.objects.all()
        return render(request=request, template_name="pages/about.html", context={"teams": teams})


def services(request):
    return render(request=request, template_name="pages/services.html", context={})


def contact(request):
    return render(request=request, template_name="pages/contact.html", context={})


def socials(request):
    socials = Social.objects.all()
    return {"socials": socials}
