from django.views.generic.edit import FormView
from users.forms import UserRegisterForm


class UserRegister(FormView):
    template_name = 'users/user_register.html'
    form_class = UserRegisterForm


    def get_context_data(self, **kwargs):
            context =  super().get_context_data(**kwargs)
            context['title_page'] = "Faça seu cadastro"

            return context

