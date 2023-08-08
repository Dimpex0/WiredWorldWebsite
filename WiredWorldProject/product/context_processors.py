from WiredWorldProject.cart.models import Cart
from WiredWorldProject.like.models import Like


def custom_processor(request):
    if request.user.is_authenticated:
        return {
            'cart_items': Cart.objects.filter(profile__client=request.user),
            'liked_items': Like.objects.filter(profile__client=request.user)
        }
    return {}
