from django.urls import path
from .views import NewYorkCreateView, BeerCreateView, NewYorkListView, BeerListView
from . import views

urlpatterns = [
    path('', views.home, name="Data_app_home"),
    path('about/', views.about, name="Data_app_about"),
    path('dashboard/', NewYorkListView.as_view(), name="data_dashboard"),
    path('tasks/',BeerListView.as_view(), name="data_tasks"),
    path('nyse/', NewYorkCreateView.as_view(), name="data_nyse"),
    path('beer/', BeerCreateView.as_view(), name="data_beer")
]