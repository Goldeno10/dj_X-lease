from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True)
    birth_date = models.DateField(null=True)
    address = models.TextField(null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, related_name='+')
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True, related_name='+')
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, related_name='+')

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
    

class State(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self) -> str:
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    IN_STOCK = "IS"
    LEASED_OUT = "LO"
    ITEM_STATUS = [
        (IN_STOCK, 'In Stock'),
        (LEASED_OUT, 'Leased Out'),
    ]
    name = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+")
    leased_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+")
    description = models.TextField(blank=True)
    item_status = models.CharField(max_length=2, choices=ITEM_STATUS, default=IN_STOCK)
    lease_period = models.IntegerField(blank=True, help_text='Leased period in Number of days')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)