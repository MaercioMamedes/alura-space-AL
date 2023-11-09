from django.views.generic.edit import FormView
from gallery.forms import AstrophotographyRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import User


class AstrophotographyRegisterView(FormView):
    form_class = AstrophotographyRegisterForm
    template_name = 'gallery/astrophotagray_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        form = AstrophotographyRegisterForm(self.request.POST, self.request.FILES)

        if form.is_valid():
            astro_image = form.save(commit=False)
            astro_image.published = True
            astro_image.registered_by = user
            astro_image.save()

        return redirect('gallery:index')
