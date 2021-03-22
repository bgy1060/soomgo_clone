from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def get_image(request, folder, file_name):
    try:
        with open('./media/' + folder + '/' + file_name, 'rb') as f:
            file_data = f.read()
    except IOError:
        return JsonResponse({"message": "FILE_NOT_EXIST"}, status=404)
    response = HttpResponse(file_data, content_type="image/png")
    return response
