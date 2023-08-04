from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch import receiver, Signal
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from WiredWorldProject import settings
from WiredWorldProject.like.models import Like
from WiredWorldProject.product.models import Product

update_product_signal = Signal()


@receiver(update_product_signal, sender=Product)
def send_restock_mail(instance, *args, **kwargs):
    try:
        pre_save_product = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return

    if pre_save_product.stock <= 0 < kwargs.get('new_stock'):
        product = instance
        product_link = kwargs.get('domain') + '/details/' + str(product.pk) + '/'

        people_that_liked_the_product = [like.profile.email for like in Like.objects.filter(product=product)]
        html_message = render_to_string('emails/restock_liked.html', {'product': product, 'product_link': product_link})
        plain_message = strip_tags(html_message)
        send_mail(
            subject=f'Restocked {product.title}',
            message=plain_message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=people_that_liked_the_product
        )
