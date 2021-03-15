from django.urls import path
from . import views

app_name = 'NguoiDung'
urlpatterns = [
    path('login/', views.LoginClass.as_view(), name='login'),
    path('register/', views.RegisterClass.as_view(), name='register'),
<<<<<<< HEAD
    path('profile/<id>', views.detail_view, name='profile'),
    path('update/<id>', views.update_view, name='update'),
=======
    path('profile/', views.ProfileClass.as_view(), name='profile'),
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
]