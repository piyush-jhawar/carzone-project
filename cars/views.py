from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page, PageNotAnInteger
from django.db.models import Q

from cars.models import Car

# Create your views here.


def cars(request):
    cars = Car.objects.order_by("-created_date").all()
    paginator = Paginator(cars, 3)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    
    search_fields = Car.objects.values('city', 'state')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    color_search = Car.objects.values_list('color', flat=True).distinct()
        
    return render(request=request, template_name='cars/cars.html', context={"cars": paged_cars, "search_fields": search_fields, "model_search": model_search, "year_search": year_search,
                                                                            "body_search": body_search, "transmission_search": transmission_search, "color_search": color_search})


def car_detail(request, id):
    single_car = get_object_or_404(Car, id=id)
    return render(request=request, template_name="cars/car_detail.html", context={'single_car': single_car})


def search(request):
    cars = Car.objects.order_by("-created_date")
    condition_search = Car.objects.values_list('condition', flat=True).distinct()
    engine_search = Car.objects.values_list('engine', flat=True).distinct()
    doors_search = Car.objects.values_list('doors', flat=True).distinct()
    passenger_search = Car.objects.values_list('passenger', flat=True).distinct()
    fueltype_search = Car.objects.values_list('fuel_type', flat=True).distinct()
    owners_search = Car.objects.values_list('no_of_owners', flat=True).distinct()
    interior_search = Car.objects.values_list('interior', flat=True).distinct()
    color_search = Car.objects.values_list('color', flat=True).distinct()
        
    
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            cars = cars.filter(Q(description__icontains=keyword) | Q(car_title__icontains=keyword))
    if 'select-model' in request.GET:
        keyword = request.GET.get('select-model')
        if keyword:
            cars = cars.filter(model__iexact=keyword)
    if 'select-location' in request.GET:
        keyword = request.GET.get('select-location')
        city, state = keyword.split(", ")
        keyword = city
        if keyword:
            cars = cars.filter(city__iexact=keyword)
    if 'select-year' in request.GET:
        keyword = request.GET.get('select-year')
        if keyword:
            cars = cars.filter(year__iexact=keyword)
    if 'select-type' in request.GET:
        keyword = request.GET.get('select-type')
        if keyword:
            cars = cars.filter(body_style__iexact=keyword)
    if 'select-transmission' in request.GET:
        keyword = request.GET.get('select-transmission')
        if keyword:
            cars = cars.filter(transmission__iexact=keyword)
    if 'select-color' in request.GET:
        keyword = request.GET.get('select-color')
        if keyword:
            cars = cars.filter(color__iexact=keyword)
    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
    if 'select-condition' in request.GET:
        keyword = request.GET.get('select-condition')
        if keyword:
            cars = cars.filter(condition__iexact=keyword)
    if 'select-engine' in request.GET:
        keyword = request.GET.get('select-engine')
        if keyword:
            cars = cars.filter(engine__icontains=keyword)
    if 'select-doors' in request.GET:
        keyword = request.GET.get('select-doors')
        if keyword:
            cars = cars.filter(doors__iexact=keyword)
    if 'select-passenger' in request.GET:
        keyword = request.GET.get('select-passenger')
        if keyword:
            cars = cars.filter(passenger__iexact=keyword)
    if 'select-fuel' in request.GET:
        keyword = request.GET.get('select-fuel')
        if keyword:
            cars = cars.filter(fuel_type__iexact=keyword)
    if 'select-owners' in request.GET:
        keyword = request.GET.get('select-owners')
        if keyword:
            cars = cars.filter(no_of_owners__iexact=keyword)
    if 'select-interior' in request.GET:
        keyword = request.GET.get('select-interior')
        if keyword:
            cars = cars.filter(interior__iexact=keyword)
    return render(request=request, template_name="cars/search.html", context={"cars": cars, "condition_search": condition_search, "engine_search": engine_search, "doors_search": doors_search,
                                                                            "passenger_search": passenger_search, "fueltype_search": fueltype_search, "owners_search": owners_search,
                                                                            "interior_search": interior_search, "color_search":color_search})

