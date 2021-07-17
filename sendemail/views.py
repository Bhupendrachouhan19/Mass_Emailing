# View Pulls Data from models.py during runtime and then process/calculate it and then it send that calculated data to a template. 

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail  # -->send_mail is a function that allows us to send an E-mail with the respective settings.
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate  # --> This django module is used for authentication.
from .models import Newsletter

# Create your views here.

def newsletter(request):
    if request.method=="POST":
         email = request.POST.get("email")
         emaillist = Newsletter(email=email)
         emaillist.save()

     #     send_mail(subject, message, from_email, to_list, fail_silently=True/False)
         subject = 'Your Sinup is Completed'
         message = 'Thankyou you for sining up to our Newsletter :)'
         from_email = settings.EMAIL_HOST_USER 
         to_list = [emaillist.email]

         send_mail(subject,message,from_email,to_list, fail_silently=False)

         return render(request, 'index.html')  #At this stage we are sending data to the template named index.html 
    
    return render(request, 'index.html')

def loginuser(request):
    if request.method=="POST":
        if "username" in request.POST:
            # If field "username" exists 
            username = request.POST.get('username')
            password = request.POST.get('password')
            # print(username, password)

            # check if user has entered correct credentials
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return render(request,'send.html')

            else:
                # No backend authenticated the credentials
                return render(request, 'login.html')
        else:
            # If "username" does not exist in request.POST
            emaillist = Newsletter.objects.all()
            print(emaillist)
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            from_email = settings.EMAIL_HOST_USER 
            to_list = emaillist.values_list("email", flat = True)
            
            to_list = list(to_list)
            print(subject, message, from_email, to_list)
            
            send_mail(subject,message,from_email,to_list, fail_silently=False)

            return render(request, 'send.html')
                
                # return render(request, 'send.html')
    return render(request, 'login.html')

