from django.urls import path
from users.views import UserRegister, LoginView, LogoutView, UserUpdateView


app_name = 'users'
urlpatterns =[
    path('register', UserRegister.as_view(), name='user_register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout',LogoutView.as_view(), name='logout'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update')
]
