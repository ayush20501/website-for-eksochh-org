from django.shortcuts import render, HttpResponse, redirect
from mooc.models import Contact,Confession,Image
from .form import ContactForm,ConfessionForm
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        data = Image.objects.all()
        return render(request, 'home.html',{'data':data})


def confess(request):
    if request.method == "POST":
        form = ConfessionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        return render(request, 'home.html')

