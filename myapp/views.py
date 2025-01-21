from django.shortcuts import render,redirect # type: ignore
from .models import*
# Create your views here.

def crud(request):
    empid=Employee.objects.all()
    print(empid)
    context={
        "empid":empid
    }
    return render(request,"crud.html",context) 

def create(request):
    if request.POST:    
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        Employee.objects.create(name=name,email=email,address=address,phone=phone)
        print(name, email, phone , address)
        return redirect('crud')
    else:
        return render(request,"crud.html")