from django.shortcuts import render, redirect
import os
from .models import Website


def create_website(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        author = request.POST['author']
        status = request.POST['status']

        Website.objects.create(title=title, description=description, image=image, author=author, status=status)
        return redirect('website_data_list')
    else:
        data = Website.objects.all()
        return render(request, 'create-website.html', {'data': data})


def website_data_list(request):
    data = Website.objects.all()
    context = {
        'data': data
    }
    return render(request, 'website-datalist.html', context)


def update_website_data(request, id):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']
        author = request.POST['author']
        status = request.POST['status']

        Website.objects.filter(id=id).update(title=title, description=description, image=image, author=author, status=status)
        return redirect('website_data_list')
    else:
        data = Website.objects.get(id=id)
        return render(request, 'update-website-data.html', {'data': data})


def delete_website_data(request, pk):
    data = Website.objects.get(id=pk)
    os.remove(data.image.path)
    data.delete()
    return redirect('website_data_list')