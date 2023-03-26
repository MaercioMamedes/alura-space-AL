from django.urls import path
from gallery.views import IndexView, AstrophotographyView, AstrophotographySearchView, AstrophotographyRegisterView


app_name = 'gallery'
urlpatterns =[
    path('', IndexView.as_view(), name='index'),
    path('object/<int:pk>/', AstrophotographyView.as_view(), name='astrophography'),
    path('buscar-imagem', AstrophotographySearchView.as_view(), name='search'),
    path('image-register/', AstrophotographyRegisterView.as_view(), name='astro_register')

]
