from django.views.generic.edit import FormView
from users.forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages



class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Faça seu Login'
        return context


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.data.get('username')
            password = form.data.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)

            

                messages.success(request, f'{user} logado com sucesso')
                return redirect('gallery:index')
        
            else:
                messages.error(request, 'Usuário ou senhas inválidos')
                return redirect('users:login')
    
    