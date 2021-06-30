from django.contrib import admin
from django.urls import path

from delivery import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('ordered/', views.OrderedView.as_view(), name='ordered'),
]

"""
– / для главной страницы
– /cart/ для корзины
– /account/ для личного кабинета
– /auth/ для аутентификации
– /register/ для регистрации
– /logout/ для выхода
– /ordered/ для подтверждения отправки
"""
