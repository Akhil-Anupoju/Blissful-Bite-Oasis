from django.shortcuts import render,redirect
from django.http import HttpResponse
from APP.models import Book_Table



# Create your views here.

def Home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,"about.html")

 
def book(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        date=request.POST.get('date')
        person=request.POST.get('persons')

        if name != '' and email!= '' and number!= '' and date!= '' and person!= '':
            data=Book_Table(Name=name,Email=email,Persons=person,Date=date,Number=number)
            data.save()
    return render(request,"book.html")

def Contact(request):
    return render(request,"contact.html")

def Menu(request):
    return render(request,"menu.html")
