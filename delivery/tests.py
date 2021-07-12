import csv
import os
from pprint import pprint

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа

from delivery import models
from delivery.models import MealCategory, Meal, Order

if __name__ == '__main__':
    pass
