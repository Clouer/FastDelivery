from delivery.scripts import get_cart_menu


def get_cart(request):
    cart_menu, total_amount = [], 0
    if request.session.get('cart') is not None:
        cart_menu = get_cart_menu(request)
        total_amount = sum([i[3] for i in cart_menu])

    return {
        'total': total_amount,
        'cart': cart_menu,
    }
