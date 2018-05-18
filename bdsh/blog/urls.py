from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('blog/', views.toBlog),
    path('images/', views.toImages),
    path('infos/', views.toInfos),
    path('products/', views.toProducts),
]