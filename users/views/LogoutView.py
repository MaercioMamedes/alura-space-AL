from django.views import View
from django.shortcuts import redirect
from django.contrib import auth


class LogoutView(View):

    def get(self, request):
        auth.logout(request)

        return redirect('gallery:index')
