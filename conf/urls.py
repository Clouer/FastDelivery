from django.contrib import admin
from django.urls import path, include

from delivery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery.urls'))
]
