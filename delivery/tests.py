import csv
import os
from pprint import pprint

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа

from delivery import models
from delivery.models import MealCategory

if __name__ == '__main__':
    main_page_menu = {}
    for category in MealCategory.objects.all():
        category_meals = category.meals.all().order_by('?').all()[:3]
        main_page_menu.update({category: category_meals})

    pprint(main_page_menu)

dict = {
    'Суши': [1, 2, 3],
    'Стритфуд': [4, 5, 6]
}
