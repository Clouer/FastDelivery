from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from delivery import forms
from delivery.models import MealCategory, User, Order
from delivery.scripts import add_meal, get_cart_menu


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'delivery/login.html'


class MySignUpView(View):
    def get(self, request):
        return render(request, 'delivery/register.html', context={
            'form': forms.SignUpForm
        })

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            User.objects.create_user(cleaned_form['username'], password=cleaned_form['password'])
            return redirect(reverse('login'))


class MainView(View):
    def get(self, request):
        main_page_menu = {}
        for category in MealCategory.objects.all():
            category_meals = category.meals.all().order_by('?').all()[:3]
            main_page_menu.update({category: category_meals})

        return render(request, 'delivery/main.html', context={
            'user': request.user,
            'menu': main_page_menu,
        })

    def post(self, request):
        meal_id = request.POST['meal']
        add_meal(request, meal_id)
        return redirect(reverse('cart'))


class CartView(View):
    def get(self, request):
        return render(request, 'delivery/cart.html')

    def post(self, request):
        meal_id = request.POST['id']
        del request.session['cart'][meal_id]
        return redirect(reverse('cart'))


class AccountView(View):
    def get(self, request):
        return render(request, 'delivery/account.html')


class OrderedView(View):
    def get(self, request):
        return redirect(reverse('main'))

    def post(self, request):
        form = request.POST
        cart = get_cart_menu(request)
        order = Order.objects.create(
            price=form['total'],
            status='new',
            email=form['email'],
            phone=form['phone'],
            address=form['address'],
            client_id=request.user.id
        )
        for meal in cart:
            order.meals.add(meal[0])

        request.session['cart'] = {}

        return render(request, 'delivery/ordered.html')
