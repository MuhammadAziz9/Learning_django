from django.urls import path
from .views import news_list,news_detail,HomePageView

urlpatterns = [
    path('',HomePageView,name='home_page'),
    path('news/',news_list,name='all_new_list'),
    path('news/<int:id>/',news_detail,name='news_detail_page')
]