from django.urls import path
from intro import views

urlpatterns = [
    path('home/', views.home),
    path('home2/', views.home2),
    path('home3/', views.home3),
    path('home4/', views.home4),
    path('home_premium/', views.home_premium),
    path('home_premium2/', views.home_premium2),
    path('web/', views.web),
    path('web2/', views.web2),
    path('number/', views.number),
    path('pizza/', views.pizza),
    path('home2022/', views.home2022),
    path('home22/', views.home22),
    path('<int:number>/', views.number_view),
    path('v1/<str:name>/', views.name_view),
    path('v2/<str:name>/', views.name_view_2),
    path('v3/<str:name>/', views.name_view_3),
]
