from django.urls import path

from . import views

app_name ='word_counter'
urlpatterns =[
    path('', views.HomePageView.as_view(), name = 'index'),
    path('counter/', views.counter, name = 'counter'),
]
