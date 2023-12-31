from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('specific', views.specific, name='specific'),

    path('getRespones',views.getRespones, name='getRespones')

    #path('article/<int:article_id>', views.article, name='article')
]