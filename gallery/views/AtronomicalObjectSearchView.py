from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse
from gallery.models import AstronomicalObject


class AtronomicalObjectSearchView(TemplateView):
    template_name = 'gallery/index.html'

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        keyword = request.POST['search']
        objects = AstronomicalObject.objects.filter(title__icontains=keyword)
        context['objects'] = objects
        return self.render_to_response(context)
