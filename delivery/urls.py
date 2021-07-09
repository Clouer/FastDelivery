from django.contrib.auth.views import LogoutView
from django.urls import path

from delivery import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.MySignUpView.as_view(), name='register'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('ordered/', views.OrderedView.as_view(), name='ordered')
]
