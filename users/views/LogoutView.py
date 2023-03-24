from django.views import View
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages


class LogoutView(View):

    def get(self, request):
        auth.logout(request)
        messages.info(request, 'logout realizado com sucesso')
        return redirect('gallery:index')
