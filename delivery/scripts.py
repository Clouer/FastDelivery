from delivery.models import Meal


def add_meal(request, meal_id):
    if request.session.get('cart') is None:
        request.session['cart'] = {}
    session_meal = request.session['cart'].get(meal_id, 0)
    request.session['cart'][meal_id] = session_meal + 1


def get_cart_menu(request):
    session = request.session['cart']
    cart_total = []
    for meal_id, amount in session.items():
        meal = Meal.objects.get(pk=meal_id)
        cart_total.append([meal.id, meal.title, amount, meal.price * amount])
    return cart_total
