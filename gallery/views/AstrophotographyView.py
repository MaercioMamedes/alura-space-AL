from django.views.generic.detail import DetailView
from gallery.models import Astrophotography


class AstrophotographyView(DetailView):
    template_name = 'gallery/imagem.html'
    model = Astrophotography

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
