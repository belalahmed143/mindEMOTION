from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('video',views.Videos,name='video'),
    path('search/',views.search, name='search'),
]
