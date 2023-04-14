from .models import CartItem

def cart_count(request):
    cart_count = CartItem.objects.count()
    return {'my_count': cart_count}