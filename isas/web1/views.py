from django.shortcuts import render


def homepage(request):
    return render(request,"web1/home1.html")
