from django.views.generic.base import TemplateView
from gallery.models import Astrophotography


class IndexView(TemplateView):
    template_name = 'gallery/index.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['objects'] = Astrophotography.objects.filter(published=True)
        
        return context
