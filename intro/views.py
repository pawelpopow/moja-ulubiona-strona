from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(
        request,
        'index.html'
    )


def home2(request):
    return HttpResponse('Witaj na stronie!')


def home3(request):
    return HttpResponse("Ta strona to jest super!")


def home4(request):
    return HttpResponse("Witam urzytkownika!")


def name_view(request, name):
    msg = f"Cześć, {name}!"
    return HttpResponse(msg)
