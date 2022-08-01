from django.shortcuts import render
from cars.models import Car

from pages.models import Team, CompanyDetail

# Create your views here.


def home(request):
    if request.method == "GET":
        teams = Team.objects.all()
        featured_cars = Car.objects.order_by(
            '-created_date').filter(is_featured=True)
        all_cars = Car.objects.order_by('-created_date').all()
        return render(request=request, template_name="pages/home.html", context={"teams": teams, "featured_cars": featured_cars, "all_cars": all_cars})
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


def companydetails(request):
    companydetails = CompanyDetail.objects.all()
    return {"companydetails": companydetails}
