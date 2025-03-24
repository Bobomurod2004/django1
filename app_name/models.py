from django.db import models

class Customers(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='customers/')
    deascription = models.TextField()


    def __str__(self):
        return self.full_name


class Partner(models.Model):
    image = models.ImageField()
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=0)



class Application(models.Model):
    class StatusChoice(models.TextChoices):
         MAIN_PAGE= 'main_page', 'MAIN_PAGE'
         SERVICE= 'service', 'SERVICE'
         GET_TT= 'get_tt', 'GET_TT'
         PARTNER = 'partner', 'PARTNER'
         ORDER = 'order', 'ORDER'


    full_name = models.CharField( max_length=255)
    phone = models.CharField( max_length=255)
    description = models.TextField( max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField( max_length=255, choices=StatusChoice.choices,default=StatusChoice.MAIN_PAGE)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField( max_length=255)
    status = models.CharField( max_length=255)
    order = models.IntegerField(default=0)
    image = models.ImageField()
    description = models.TextField( max_length=255, null=True, blank=True)
    brand = models.CharField( max_length=255)
    country = models.CharField( max_length=255)
    guarantee = models.CharField( max_length=255)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
    is_main_page = models.BooleanField( max_length=255)


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE
    )


class ProductCharacteristic(models.Model):
    key = models.CharField( max_length=255)
    value = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    product = models.ForeignKey(
        Product, related_name='product_characteristic', on_delete=models.CASCADE
    )

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    order = models.IntegerField(default=0)

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    image = models.ImageField()
    date = models.DateField()
    body = models.TextField(max_length=255)


class Korgazmalar(models.Model):
    titte = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    image = models.ImageField(upload_to='customers/')


class Achievements(models.Model):
    icon = models.ImageField()
    text = models.TextField(max_length=255)
    order = models.IntegerField(default=0)


class Buyrs(models.Model):
    icon = models.ImageField()
    order = models.IntegerField(default=0)


class Jamoa(models.Model):
    titte = models.CharField(max_length=255)
    text = models.TextField(max_length=255)


class OurTem(models.Model):
    image = models.ImageField(upload_to='customers/')
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    order = models.IntegerField(default=0)



class Galareyia(models.Model):
    url = models.URLField()
    text = models.TextField(max_length=255)
    order = models.IntegerField(default=0)
