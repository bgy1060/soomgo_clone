from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Region
from .serializers import *
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def region_list(request):
    query_set = Region.objects.all()
    serializer = RegionSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


def detail_region(request, region_name):
    region_id = Region.objects.get(name=region_name)
    detail_cat = DetailRegion.objects.filter(region=region_id.id)
    serializer = DetailRegionSerializer(detail_cat, many=True)
    return JsonResponse(serializer.data, safe=False)

