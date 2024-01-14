from django.shortcuts import render, redirect
from .models import Classes
import os
from .forms import Classes_Form
from django.contrib import messages
from django.core.paginator import Paginator


def create_class_data(request):
    if request.method == "POST":
        form = Classes_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Created')
            return redirect('class_data_list')
        else:
            messages.error(request,'Invalid data')
            return redirect(create_class_data)
    else:
        form = Classes_Form()
        return render(request,'create-class-data.html',{'form':form})


def class_data_list(request):
    data = Classes.objects.all().order_by('-id').values("id","description","image", "status", "title", "url")
    paginator = Paginator(data,2)
    page_number = request.GET.get('page')
    data_page_objects = paginator.get_page(page_number)
    return render(request,'class-data-list.html',{'data':data_page_objects})


def update_class_data(request,id):
    object = Classes.objects.get(id=id)
    if request.method == "POST":
        form = Classes_Form(request.POST,request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('class_data_list')
        else:
            return redirect('update_class_data',id)
    else:
        object = Classes.objects.get(id=id)
        form = Classes_Form(instance=object)
        return render(request,'update-class-data.html',{'form':form})

def delete_class_data(request,pk):
    data = Classes.objects.get(id=pk)
    os.remove(data.image.path)
    data.delete()
    return redirect('class_data_list')


