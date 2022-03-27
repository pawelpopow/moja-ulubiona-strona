from django.shortcuts import render


def new(request, news):
    return render(
        request,
        'draw/news.html',
        context={
            'news': news
        }
    )
