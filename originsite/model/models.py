from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Actor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.CharField(primary_key=True, max_length=4)
    address = models.CharField(max_length=50)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', models.DO_NOTHING)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    category_id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    city_id = models.CharField(primary_key=True, max_length=4)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=4)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=4)
    store_id = models.CharField(max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('customer_id', 'store_id', 'address', 'last_name'),)


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, models.DO_NOTHING, primary_key=True)
    film_id = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor', 'film_id'),)


class FilmCategory(models.Model):
    film_id = models.CharField(primary_key=True, max_length=8)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film_id', 'category'),)


class FilmText(models.Model):
    film_id = models.CharField(primary_key=True, max_length=4)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_text'


class Films(models.Model):
    film_id = models.CharField(primary_key=True, max_length=4)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Languages', models.DO_NOTHING)
    original_language = models.ForeignKey('Languages', models.DO_NOTHING, blank=True, null=True)
    rental_duration = models.CharField(max_length=8)
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    lengths = models.CharField(max_length=8, blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=32, blank=True, null=True)
    special_features = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'films'
        unique_together = (('film_id', 'title', 'language'),)


class Inventory(models.Model):
    inventory_id = models.CharField(primary_key=True, max_length=4)
    film_id = models.CharField(max_length=4)
    store_id = models.CharField(max_length=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'
        unique_together = (('inventory_id', 'film_id', 'store_id'),)


class Languages(models.Model):
    language_id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'languages'


class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=8)
    customer_id = models.CharField(max_length=8)
    staff_id = models.CharField(max_length=8)
    rental_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'
        unique_together = (('payment_id', 'staff_id', 'customer_id'),)


class Rental(models.Model):
    rental_id = models.CharField(primary_key=True, max_length=8)
    rental_date = models.DateTimeField()
    inventory_id = models.CharField(max_length=8)
    customer_id = models.CharField(max_length=8)
    return_date = models.DateTimeField(blank=True, null=True)
    staff_id = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_id', 'rental_date', 'inventory_id', 'customer_id'),)


class Staff(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=4)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    picture = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.CharField(max_length=4)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'
        unique_together = (('staff_id', 'store_id', 'address'),)


class Store(models.Model):
    store_id = models.CharField(primary_key=True, max_length=4)
    manager_staff_id = models.CharField(max_length=4)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'
        unique_together = (('store_id', 'manager_staff_id', 'address'),)