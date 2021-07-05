from django.shortcuts import render
from django.views import View

from delivery.models import MealCategory


class MainView(View):
    def get(self, request):
        main_page_menu = {}
        for category in MealCategory.objects.all():
            category_meals = category.meals.all().order_by('?').all()[:3]
            main_page_menu.update({category: category_meals})

        return render(request, 'delivery/main.html', context={
            'menu': main_page_menu
        })


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
