from django.urls import path
from gallery.views import IndexView, AstrophotographyView, AstrophotographySearchView


app_name = 'gallery'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('object/<int:pk>/', AstrophotographyView.as_view(), name='astrophography'),
    path('buscar-imagem', AstrophotographySearchView.as_view(), name='search'),

]
