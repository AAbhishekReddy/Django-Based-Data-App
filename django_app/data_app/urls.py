from django.urls import include, path
from rest_framework import routers

from .views import NewYorkCreateView, BeerCreateView, NewYorkListView, BeerListView
from . import views
from .api.views import NewYorkViewSet, BeerViewSet, NYSEPredict, BeerPredict

router = routers.DefaultRouter()
router.register(r'nyse', NYSEPredict)
router.register(r'beer_predict', BeerPredict)


urlpatterns = [
    path('', views.home, name="Data_app_home"),
    path('about/', views.about, name="Data_app_about"),
    path('dashboard/', NewYorkListView.as_view(), name="data_dashboard"),
    path('tasks/',BeerListView.as_view(), name="data_tasks"),
    path('nyse/', NewYorkCreateView.as_view(), name="data_nyse"),
    path('beer/', BeerCreateView.as_view(), name="data_beer"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/nyse/', NYSEPredict.as_view(), name = 'nyse_predict'),
    # path('api/beer_predict/', BeerPredict.as_view(), name = 'beer_predict'),
    path('api/new_york/', NewYorkViewSet.as_view(), name = 'new_york'),
    path('api/beer/', BeerViewSet.as_view(), name = 'beer'),
    path('api/', include(router.urls)),

]