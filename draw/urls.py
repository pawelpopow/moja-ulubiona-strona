from django.urls import path

from draw import views

app_name = 'draw'

urlpatterns = [
    path('new/', views.new, name='new'),
]
