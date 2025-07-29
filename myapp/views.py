from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.db.models import Q

# Create your views here.
def home_page(request):
    query = request.GET.get('search')
    if query:
        data = Student.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) 
        )
    else:
        data = Student.objects.all()
    context = {
        'data':data,
    }
    return render(request,'home.html',context)

def insert(request):
    print("1")
    if request.method == 'POST':
        print("2")
        name_ = request.POST['name']
        email_ = request.POST['email']
        city_ = request.POST['city']
        phone_ = request.POST['phone']
        
        
        data = Student.objects.create(
            name = name_,
            email = email_,
            city = city_,
            phone = phone_
        )
        
        data.save()
        
        return redirect('home_page')
        
        
    return render(request,'home.html')

def update(request,id):
    print("1")
    data = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        print("2")
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.city = request.POST['city']
        data.phone = request.POST['phone']
        
        data.save()
        
        return redirect('home_page')
        
        
    return render(request,'home.html')


def delete(request,id):
    data = get_object_or_404(Student,id=id)
    data.delete()
    return redirect('home_page')

