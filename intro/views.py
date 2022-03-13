from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(
        request,
        'index.html'
    )


def home_premium(request):
    return HttpResponse('Ta strona jest pod kontrola CBA !!!')


def home_premium2(request):
    return HttpResponse('To jest fajna strona fajnie, że tu jesteś !!!')


def home2(request):
    return HttpResponse('Witaj na stronie!')


def home3(request):
    return HttpResponse("Ta strona to jest super!")


def home4(request):
    return HttpResponse("Witam użytkownika strony!")


def name_view(request, name):
    msg = f"Cześć, {name}!"
    return HttpResponse(msg)
