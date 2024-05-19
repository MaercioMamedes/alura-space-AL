from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User


class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "email"]
    template_name = "users/user_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Atualização de cadastro de usuário"

        return context
