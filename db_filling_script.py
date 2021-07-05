import csv
import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа

from delivery import models

if __name__ == '__main__':

    with open('delivery_categories.csv', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        for i in csv_file:
            models.MealCategory.objects.create(
                id=int(i[0]),
                title=i[1]
            )

    with open('delivery_items.csv', encoding='utf-8') as file:
        csv_file = csv.reader(file)
        for i in csv_file:
            models.Meal.objects.create(
                id=int(i[0]),
                title=i[1],
                price=int(i[2]),
                description=i[3],
                picture=i[4],
                category_id=int(i[5])
            )
