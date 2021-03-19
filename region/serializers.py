from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class DetailRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailRegion
        fields = ['detail_name']
