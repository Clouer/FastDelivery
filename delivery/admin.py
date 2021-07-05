from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from delivery.models import User, MealCategory, Order, Meal


class MealCategoriesAdmin(admin.ModelAdmin):
    pass


class MealAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(MealCategory, MealCategoriesAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Order, OrderAdmin)
