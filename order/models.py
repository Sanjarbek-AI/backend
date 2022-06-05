from django.db import models


class OrderStatus(models.IntegerChoices):
    ACCEPTED = 1
    NOT_ACCEPTED = 0
    ON_THE_WAY = 2
    DELETED = -1


class OrderType(models.IntegerChoices):
    PUBLIC = 1
    PRIVATE = 0


class OrderModel(models.Model):
    """ Order model to store data in the database """
    user_id = models.IntegerField(verbose_name="User id", blank=True, null=True)
    total_product = models.IntegerField(verbose_name="Total product", blank=True, null=True)
    total_price = models.FloatField(verbose_name="Total price", blank=True, null=True)
    description = models.CharField(max_length=512, verbose_name="Description for order", blank=True, null=True)
    location = models.CharField(max_length=255, verbose_name="Location of order", blank=True, null=True)
    price = 0
    status = models.SmallIntegerField("Status", choices=OrderStatus.choices, default=OrderStatus.NOT_ACCEPTED)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Rewritten object display method """
        return f"Order: {self.id}, {self.price}"

    class Meta:
        """ Class Meta """
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItemModel(models.Model):
    """ order items model to store data in the database """
    product_id = models.IntegerField(verbose_name="product id", blank=True, null=True)
    order_id = models.IntegerField(verbose_name="order id", blank=True, null=True)

    quantity = models.IntegerField(verbose_name="user id", blank=True, null=True)
    product_price = models.FloatField(verbose_name="price", blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Rewritten object display method """
        return f"Order: {self.product_id.title}, {self.product_price}"

    class Meta:
        """ Class Meta """
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
