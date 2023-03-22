from django.views.generic.detail import DetailView
from gallery.models import AstronomicalObject


class AstronomicalObjectView(DetailView):
    template_name = 'gallery/imagem.html'
    model = AstronomicalObject

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
