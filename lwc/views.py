# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {}
    tempalte = "home.html"
    return render(request, tempalte, context)
    # return HttpResponse("Hello, world. You're at the polls index.")