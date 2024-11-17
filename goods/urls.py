from django.urls import path


from . import  views

app_name = 'goods'
urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.services, name='service'),
    path('starter/', views.starter, name='starter'),
    path('layout/', views.layout, name='layout'),

]