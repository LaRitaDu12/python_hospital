from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.welcome, name='welcome'),
    path('who/', views.who, name='who'),
    path('context/', views.context, name='context'),
    path('dataviz/', views.dataviz, name='dataviz'),
    path('<int:visu_id>/visu/', views.visu, name='visu'),
    path('models/', views.models, name='models'),
    path('<int:pred_id>/pred/', views.pred, name='pred'),

]