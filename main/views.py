from django.http import HttpResponse
from django.shortcuts import render
# def home_page(request):
#     return HttpResponse('<h1 style= "color:white; background-color:black; height: 100vh; text-align: center;">This is the main home page</h1>')

def home_page(request):
    return render(request, "../templates/index.html")