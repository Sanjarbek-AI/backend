from django.db import models


class ColorModel(models.Model):
    """ Model to store Colors data"""
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='Color code')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Color title')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} | {self.title}"

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class SizeModel(models.Model):
    """ Model to store Colors data"""
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Size')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class GenderChoice(models.IntegerChoices):
    MEN = 1
    WOMEN = 0
    OTHER = 2


class CategoryModel(models.Model):
    """ Model to store Colors data"""
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Category title')
    image = models.ImageField(upload_to='media/category/', verbose_name='category image', null=True, blank=True)
    gender = models.SmallIntegerField("GenderChoice", choices=GenderChoice.choices, default=GenderChoice.OTHER)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.gender}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ProductStatus(models.IntegerChoices):
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1


class StoreStatus(models.IntegerChoices):
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1


class PeopleType(models.IntegerChoices):
    Male = 0
    Female = 1
    Kids = 2
    NOT_SELECTED = -1


class StoreModel(models.Model):
    """ Product model to store data in the database """
    logo = models.ImageField(upload_to='media/store/logo', verbose_name='Brand logo', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Name", unique=True, blank=False, null=False)
    description = models.CharField(max_length=512, verbose_name="Description", blank=True, null=True)
    location = models.CharField(max_length=512, verbose_name="Location title", blank=True, null=True)
    location_link = models.CharField(max_length=512, verbose_name="Location link", blank=True, null=True)
    gender = models.SmallIntegerField("GenderChoice", choices=GenderChoice.choices, default=GenderChoice.OTHER)
    status = models.SmallIntegerField("Status", choices=StoreStatus.choices, default=StoreStatus.INACTIVE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.gender}'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ProductModel(models.Model):
    """ Product model to store data in the database """
    categories = models.ManyToManyField(CategoryModel, related_name='product', verbose_name='Categories')
    colors = models.ManyToManyField(ColorModel, related_name='product', verbose_name='Colors')
    sizes = models.ManyToManyField(SizeModel, related_name='product', verbose_name='Sizes')
    store = models.ForeignKey(StoreModel, on_delete=models.CASCADE, related_name='product', verbose_name='Store')

    title = models.CharField(max_length=255, verbose_name="Title", unique=True, blank=False, null=False)
    description = models.CharField(max_length=512, verbose_name="Description", blank=True, null=True)

    price = models.FloatField(verbose_name="price", blank=True, null=True)
    status = models.SmallIntegerField("Status", choices=ProductStatus.choices, default=ProductStatus.INACTIVE)
    people_type = models.SmallIntegerField("PeopleType", choices=PeopleType.choices, default=PeopleType.NOT_SELECTED)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Rewritten object display method """
        return f"Product: {self.title}, {self.price}"

    class Meta:
        """ Class Meta """
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        ProductModel,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='product'
    )
    image = models.ImageField(upload_to='media/products', verbose_name='image')
    description = models.CharField(max_length=255, verbose_name='Description for image', null=True, blank=True)

    def __str__(self):
        return f'{self.product.title} | {self.description}'

    class Meta:
        """ Class Meta """
        verbose_name = 'Product images'
        verbose_name_plural = 'Products images'


class WishlistModel(models.Model):
    """ Product model to store data in the database """
    product_id = models.IntegerField(verbose_name="Product id", blank=True, null=True)
    user_id = models.IntegerField(verbose_name="User id", blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Rewritten object display method """
        return f"Wishlist: {self.product_id}, {self.user_id}"

    class Meta:
        """ Class Meta """
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
