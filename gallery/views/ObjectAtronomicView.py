from django.views.generic.base import TemplateView


class ObjectAtronomicView(TemplateView):
    template_name = 'gallery/imagem.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
