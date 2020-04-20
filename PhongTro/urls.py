from django.urls import path
from . import views

app_name = 'PhongTro'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.save_news_class.as_view(), name='add'),
    path('gets/', views.getAll.as_view(), name='getall'),
    path('detail/<int:PhongTro_id>', views.getdetail.as_view(), name='detail'),
]