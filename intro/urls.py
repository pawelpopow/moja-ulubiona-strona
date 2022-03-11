from django.urls import path
from intro import views


urlpatterns = [
    path('home/', views.home),
    path('home2/', views.home2),
    path('home3/', views.home3),
    path('home4/', views.home4),
    path('<str:name>/', views.name_view),
]


