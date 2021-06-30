from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'delivery/main.html')


class CartView(View):
    def get(self, request):
        return render(request, 'delivery/cart.html')


class AccountView(View):
    def get(self, request):
        return render(request, 'delivery/account.html')


class AuthView(View):
    def get(self, request):
        return render(request, 'delivery/auth.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'delivery/register.html')


class LogoutView(View):
    pass


class OrderedView(View):
    def get(self, request):
        return render(request, 'delivery/ordered.html')
