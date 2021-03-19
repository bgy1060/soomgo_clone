from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category
from .serializers import *
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def category_list(request):
    query_set = Category.objects.all()
    serializer = CategorySerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


def detail_category(request, cat_name):
    cat_name = cat_name.replace('-', '/')
    cat_name = cat_name.strip()
    cat_id = Category.objects.get(name=cat_name)
    detail_cat = DetailCategory.objects.filter(category=cat_id.id)
    serializer = DetailCategorySerializer(detail_cat, many=True)
    return JsonResponse(serializer.data, safe=False)


def sub_category(request, cat_name, detail_name):
    detail_name = detail_name.replace('-', '/')
    detail_name = detail_name.strip()
    detail_id = DetailCategory.objects.get(detail_name=detail_name)
    sub_cat = SubCategory.objects.filter(detail_category_id=detail_id)
    serializer = SubCategorySerializer(sub_cat, many=True)
    return JsonResponse(serializer.data, safe=False)
