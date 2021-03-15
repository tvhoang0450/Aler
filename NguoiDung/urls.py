from django.urls import path
from . import views

app_name = 'NguoiDung'
urlpatterns = [
    path('login/', views.LoginClass.as_view(), name='login'),
    path('register/', views.RegisterClass.as_view(), name='register'),
    path('profile/<id>', views.detail_view, name='profile'),
    path('update/<id>', views.update_view, name='update'),
]