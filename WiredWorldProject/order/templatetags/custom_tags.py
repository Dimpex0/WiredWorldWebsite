from django import template

register = template.Library()


@register.filter(name='getOrderDate')
def getOrderDate(order_list):
    return order_list[0].date


@register.filter(name='getOrderTotal')
def getOrderTotal(order_list):
    total = 0
    for order in order_list:
        total += float(order.product.price) * float(order.quantity)
    return f"{total:.02f}"
