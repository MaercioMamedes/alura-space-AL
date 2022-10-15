from django.urls import path
from gallery.views import index, object_astronomic

app_name = 'gallery'
urlpatterns =[
    path('', index, name='index'),
    path('object', object_astronomic, name='object_astronomic'),

]
