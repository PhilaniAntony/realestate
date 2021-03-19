from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor

# Register your models here.


class Listing(models.Model):
    SALE_TYPE = (
        ("For Sale", "For Sale"),
        ("To Rent", "To Rent"),

    )
    HOME_TYPE = (
        ("House", "House"),
        ("Condo", "Condo"),
        ("Townhouse", "Townhouse"),
    )
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(
        max_length=50, choices=HOME_TYPE, default='House')
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    # main photo
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # addtional photos
    photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_two = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_three = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_four = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_five = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_six = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_seven = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_eight = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_nine = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_ten = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # address
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=15)

    sale_type = models.CharField(
        max_length=50, choices=SALE_TYPE, default='For Sale')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
