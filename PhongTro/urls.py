from django.urls import path
from . import views

app_name = 'PhongTro'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.post, name='add'),
    path('gets/', views.getAll.as_view(), name='getall'),
    path('detail/<int:PhongTro_id>', views.getdetail.as_view(), name='detail'),
    path('edit/<int:pk>', views.PhongTroUpdate.as_view(), name='phongtro_edit'),
    path('delete/<int:pk>', views.PhongTroDelete.as_view(), name='phongtro_delete'),

    path('ajax/load-huyen/', views.load_huyen, name='ajax_load_districts'),
    path('ajax/load-xa/', views.load_xa, name='ajax_load_wards'),
    path('ajax/load-duong/', views.load_duong, name='ajax_load_streets')
]