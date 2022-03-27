from django.urls import path

from mem import views

app_name = 'mem'

urlpatterns = [
    path('name2/', views.name2, name='name2'),
]
