from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crawling/', views.crawling_index, name='crawling_index'),
    path('crawling/search', views.search, name='search'),
]
