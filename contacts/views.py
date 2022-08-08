from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from contacts.models import Contact
from django.urls import reverse
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        try:
            car = Car.objects.get(car_title=car_title)
        except:
            messages.error(request=request, message="Title Chnaged")
            return redirect(reverse('cars'))

        if request.user.is_authenticated:
            if int(user_id) == request.user.id and int(car_id) == car.id:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
                if has_contacted:
                    messages.error(
                        request=request, message="You have already made an inquiry about this car. Please wait until we get back to you.")
                    return redirect(reverse('car_detail', args=(car_id,)))
                else:
                    contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
                                      state=state, email=email, phone=phone, message=message)
                    
                    admin_info = User.objects.get(is_superuser=True)
                    admin_email = admin_info.email

                    send_mail(
                        'New Car Inquiry',
                        'You have a new inquiry for the car ' + car_title +
                        '. Please login to your admin panel for more info.',
                        '',
                        [admin_email],
                        fail_silently=False,
                    )
                    contact.save()
                    messages.success(
                        request=request, message="Your request has been submitted, we will get back to you shortly.")
                    # return redirect('/cars/'+ car_id)
                    return redirect(reverse('car_detail', args=(car_id,)))
            else:
                messages.error(request=request,
                               message="Client Manipulated User/Car Id")
                return redirect(reverse('cars'))
