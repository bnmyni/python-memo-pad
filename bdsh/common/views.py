from django.shortcuts import render

# Create your views here.

def declare(request):
    return render(request, 'common/declare.html')