from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page, PageNotAnInteger

from cars.models import Car

# Create your views here.


def cars(request):
    cars = Car.objects.order_by("-created_date").all()
    paginator = Paginator(cars, 1)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", paged_cars)
    return render(request=request, template_name='cars/cars.html', context={"cars": paged_cars})


def car_detail(request, id):
    single_car = get_object_or_404(Car, id=id)
    return render(request=request, template_name="cars/car_detail.html", context={'single_car': single_car})
    