from django.urls import path
from gallery.views import IndexView, AstronomicalObjectView, AtronomicalObjectSearchView


app_name = 'gallery'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('object/<int:pk>/', AstronomicalObjectView.as_view(), name='astronomical_object'),
    path('buscar-imagem', AtronomicalObjectSearchView.as_view(), name='search'),

]
