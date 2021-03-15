from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('/about', views.About.as_view(), name='about'),
    path('/contact', views.Contact.as_view(), name='contact'),
    path('/huongdan', views.HuongDan.as_view(), name='huongdan')
]