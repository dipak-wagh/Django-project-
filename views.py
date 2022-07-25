from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import Book


def show_data(request):

    return render(request,"show-data.html",{"book":Book.objects.all()})