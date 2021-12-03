from django import forms
from django.core.checks import messages
from django.db.models.fields import NOT_PROVIDED
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, request
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import PaymentForm, ReserveTable
from django.contrib.auth.models import User

# Create your views here.
def index(response, id):
    return render(response, "base.html",{})

def homepage(response):
    return render(response, "homepage.html",{})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']  
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # messages.info(request, 'invalid credentials')
            return redirect('homepage')
    else:
        return render(request, 'login_user.html')
    
    

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/register')
            else:
                user = User.objects.create(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User created')
                return redirect('/register')   
        else:
            messages.info(request,'password not matching')
        return redirect('/register')
        
    else:
        return render(request, 'register.html')



def reserve(response):
    if response.method == "POST":
        form = ReserveTable(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/payment", {'form':form})
    else:
        form = ReserveTable()
        
    return render(response, "reserve.html",{"form":form})


def paymentmodule(response):
    if response.method == "POST":
        form = PaymentForm(response.POST)
        if form.is_valid():
            return redirect("/confirmation")
    else:
        form = PaymentForm()
    
    return render(response, "payment.html", {'form':form})

def confirmation(response):
    return render(response, "confirmation.html",{})