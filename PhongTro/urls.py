from django.urls import path
from . import views

app_name = 'PhongTro'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.save_news_class.as_view(), name='add'),
    path('gets/', views.getAll.as_view(), name='getall'),
    path('detail/<int:PhongTro_id>', views.getdetail.as_view(), name='detail'),

    path('ajax/load-huyen/', views.load_huyen, name='ajax_load_districts'),
    path('ajax/load-xa/', views.load_xa, name='ajax_load_wards'),
    path('ajax/load-duong/', views.load_duong, name='ajax_load_streets')
]