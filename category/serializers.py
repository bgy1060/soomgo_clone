from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class DetailCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailCategory
        fields = ['detail_name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['sub_name']