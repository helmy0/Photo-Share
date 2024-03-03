from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.


def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name__contains=category)

    categories = Category.objects.all()


    context = {
        'categories': categories,
        'photos': photos,
    }
    return render(request, "photos/gallery.html", context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, "photos/photo.html", {'photo': photo})

def addPhoto(request):
    categories = Category.objects.filter()

    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('img')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new-category'] != '':
            category, created = Category.objects.get_or_create(name=data['new-category'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description= data['description'],
            image = img,
        )
        return redirect('gallery')
    context = {
        'categories': categories,
    }

    return render(request, "photos/add.html", context)


def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('/')
    context = {
        'photo': photo,
    }
    return render(request, "photos/delete.html", context)