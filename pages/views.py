from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse

from pages.models import Team, CompanyDetail
from cars.models import Car


# Create your views here.


def home(request):
    if request.method == "GET":
        teams = Team.objects.all()
        featured_cars = Car.objects.order_by(
            '-created_date').filter(is_featured=True)
        all_cars = Car.objects.order_by('-created_date').all()
        search_fields = Car.objects.values('city', 'state')
        # year = Car.objects.distinct('year')
        model_search = Car.objects.values_list('model', flat=True).distinct()
        city_search = Car.objects.values_list('city', flat=True).distinct()
        year_search = Car.objects.values_list('year', flat=True).distinct()
        body_search = Car.objects.values_list(
            'body_style', flat=True).distinct()
        return render(request=request, template_name="pages/home.html", context={"teams": teams, "featured_cars": featured_cars, "all_cars": all_cars,
                                                                                 "search_fields": search_fields, "model_search": model_search,  "city_search": city_search,  "year_search": year_search,  "body_search": body_search})
    elif request.method == "POST":
        pass


def about(request):
    if request.method == "GET":
        teams = Team.objects.all()
        return render(request=request, template_name="pages/about.html", context={"teams": teams})


def services(request):
    return render(request=request, template_name="pages/services.html", context={})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + \
            '. Phone: ' + phone + '. Message: ' + message
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            '',
            [admin_email],
            fail_silently=False,
        )
        messages.success(
            request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect(reverse('contact'))

    return render(request=request, template_name="pages/contact.html", context={})


def companydetails(request):
    companydetails = CompanyDetail.objects.all()
    return {"companydetails": companydetails}
