from django.urls import path

from mem import views

app_name = 'mem'

urlpatterns = [
    path('img/', views.images, name='images'),
]
