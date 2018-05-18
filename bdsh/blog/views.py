from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'portal/blog/index.html')


def toBlog(request):
    return render(request, 'portal/blog/blog.html')

def toImages(request):
    return render(request, 'portal/blog/images.html')

def toInfos(request):
    return render(request, 'portal/blog/infos.html')

def toProducts(request):
    return render(request, 'portal/blog/products.html')