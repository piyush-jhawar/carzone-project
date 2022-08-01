from django.shortcuts import render

# Create your views here.


def cars(request):
    return render(request=request, template_name='cars/cars.html', context={})