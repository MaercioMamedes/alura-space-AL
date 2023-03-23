from django.urls import path
from users.views import UserRegister


app_name = 'gallery'
urlpatterns =[
    path('register', UserRegister.as_view(), name='user_register'),

]