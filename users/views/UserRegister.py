from django.views.generic.edit import FormView
from users.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages


class UserRegister(FormView):
    template_name = 'users/user_register.html'
    form_class = UserRegisterForm


    def get_context_data(self, **kwargs):
            context =  super().get_context_data(**kwargs)
            context['title_page'] = "Faça seu cadastro"

            return context


    def post(self, request):
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                first_name = form.data.get('first_name')
                last_name = form.data.get('last_name')
                username = form.data.get('username')
                email = form.data.get('email')
                password = form.data.get('password')

                user = User.objects.create(
                      first_name=first_name,
                      last_name=last_name,
                      username=username,
                      email=email
                )

                user.set_password(password)
                user.save()



            messages.success(request, "Cadastro realizado com sucesso")
            return redirect('users:login')
