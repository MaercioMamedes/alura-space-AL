from django.urls import path
from gallery.views import IndexView, AstronomicalObjectView


app_name = 'gallery'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('object', AstronomicalObjectView.as_view(), name='object_astronomic'),

]
