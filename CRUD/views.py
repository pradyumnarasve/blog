from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Details
from .forms import DetailsForm


# Create your views here.

def index(request):
    return render(request,'blog16/index.html')

def create(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=Details.objects.create(name=name, age=age, address=address)
        obj.save()
        return redirect('/')
        
def retrieve(request):
    details = Details.objects.all()
    return render(request,'blog16/retrieve.html',{'details':details})

def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request, "blog16/edit.html",{'object':object})

def updateData(request,id):
    print("IN update")
    object=Details.objects.get(id=id)
    print(object,"Obj")
    form=DetailsForm(request.POST,instance=object)
    print("111")
    if form.is_valid():
        form.save()
        # object=Details.objects.all()
        return redirect('retrieve')
    return HttpResponse(str(form.errors))
    
def delete(request,id):   
        Details.objects.filter(id=id).delete()
        return redirect('retrieve')