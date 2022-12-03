from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    print("this is my first jango application")
    return HttpResponse("<h1> this is my heading in jango framework </h1>")


def homePage(request):
    if request.method == 'POST':
        varr = request.POST['uname']
        print(varr)
        varr = request.POST['urate']
        print(varr)
        varr = request.POST['uquan']
        print(varr)
    return render(request, "home.html")


def regis(request):
    return render(request, "regis.html")


def formIndex(request):
    return render(request, "index.html")
