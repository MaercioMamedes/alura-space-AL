from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'gallery/index.html'

    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)
