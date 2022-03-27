from django.shortcuts import render


def name2(request, name):
    return render(
        request,
        'mem/name.html',
        context={
            'name': name
        }
    )
