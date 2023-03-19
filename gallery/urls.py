from django.urls import path
from gallery.views import IndexView, ObjectAtronomicView


app_name = 'gallery'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('object', ObjectAtronomicView.as_view(), name='object_astronomic'),

]
