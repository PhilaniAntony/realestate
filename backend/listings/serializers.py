from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'price', 'sale_type',
                  'bedrooms', 'sqft', 'photo_main', 'slug')


class listingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'
