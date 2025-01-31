from django.urls import path
from .views import news_list,news_detail

urlpatterns = [
    path('',news_list,name='all_new_list'),
    path('<int:id>/',news_detail,name='news_detail_page')
]