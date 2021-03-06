from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(
        request,
        'index.html'
    )


def home2022(request):
    return render(
        request,
        'base.html'
    )


def home22(request):
    return render(
        request,
        'index1.html'
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


def web(request):
    return HttpResponse("Ta strona jest nowa !!!!")


def web2(request):
    return HttpResponse("Przepraszamy wystąpił chwilowy błąd !!!!!")


def number_view(request, number):
    qse = f"Moj szczesliwy numer to: {number}!"
    return HttpResponse(qse)


def name_view(request, name):
    msg = f"Cześć, {name}!"
    return HttpResponse(msg)


def number(request):
    return HttpResponse("Twój szczesliwy number jest dziś 14 a wczoraj był 12 ")


def pizza(request):
    return HttpResponse("Cena pizzy jest tania dzisiaj a wczoraj była droga!!!!!!!!!!!")


def name_view_2(request, name):
    return render(
        request,
        'intro/name.html',
        context={
            'name': name
        }
    )


def name_view_3(request, name):
    return render(
        request,
        'intro/home.html',
        context={
            'name': name
        }
    )
