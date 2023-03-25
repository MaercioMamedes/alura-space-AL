from django.views.generic import TemplateView
from gallery.models import Astrophotography


class AstrophotographySearchView(TemplateView):
    template_name = 'gallery/index.html'

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword = request.POST['search']
        objects = Astrophotography.objects.filter(title__icontains=keyword)
        context['objects'] = objects
        return self.render_to_response(context)
