from django.shortcuts import render


def images(request, img):
    return render(
        request,
        'mem/images.html',
        context={
            'img': img
        }
    )
