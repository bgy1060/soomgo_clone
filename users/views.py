from django.db.models import Count, Avg, Sum
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from category.models import Category
from .models import *
from .serializers import *
import re


# Create your views here.

def region_user(request, region_name):
    if region_name == '전국':
        query_set = User.objects.prefetch_related('user_question', 'reviewer_question'). \
            annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).all()

    else:
        if re.search(r'전체', region_name):
            region_name = region_name[:2]
            region_id = Region.objects.get(name=region_name)
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                filter(region=region_id)
        else:
            detail_region_id = DetailRegion.objects.get(detail_name=region_name)
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                filter(detail_region=detail_region_id)

    serializer = UserSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


def cat_user(request, cat_name):
    cat_name = cat_name.replace('-', '/')

    if cat_name == '서비스 전체':
        query_set = User.objects.prefetch_related('user_question'). \
            annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).all()

    else:
        if re.search(r'전체', cat_name):
            cat_name = cat_name[:-2].strip()
            check = Category.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')) \
                .filter(name=cat_name)
            if check.exists():
                cat_id = Category.objects.get(name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                    filter(category=cat_id)

            else:
                detail_cat_id = DetailCategory.objects.get(detail_name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).filter(
                    detail_category=detail_cat_id)
        else:
            sub_cat_id = SubCategory.objects.get(sub_name=cat_name)
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                filter(sub_category=sub_cat_id)

    serializer = UserSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


def region_cat_user(request, region_name, cat_name):
    cat_name = cat_name.replace('-', '/')
    if region_name == '전국' or cat_name == '서비스 전체':
        if region_name == '전국' and cat_name == '서비스 전체':
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).all()
        elif region_name == '전국' and not (cat_name == '서비스 전체'):
            if re.search(r'전체', cat_name):
                cat_name = cat_name[:-2].strip()
                check = Category.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')) \
                    .filter(name=cat_name)
                if check.exists():
                    cat_id = Category.objects.get(name=cat_name)
                    query_set = User.objects.prefetch_related('user_question'). \
                        annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                        filter(category=cat_id)

                else:
                    detail_cat_id = DetailCategory.objects.get(detail_name=cat_name)
                    query_set = User.objects.prefetch_related('user_question'). \
                        annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).filter(
                        detail_category=detail_cat_id)
            else:
                sub_cat_id = SubCategory.objects.get(sub_name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                    filter(sub_category=sub_cat_id)
        else :
            if re.search(r'전체', region_name):
                region_name = region_name[:2]
                region_id = Region.objects.get(name=region_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                    filter(region=region_id)
            else:
                detail_region_id = DetailRegion.objects.get(detail_name=region_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')). \
                    filter(detail_region=detail_region_id)

    else:
        if re.search(r'전체', region_name) and re.search(r'전체', cat_name):
            cat_name = cat_name[:-2].strip()
            check = Category.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                filter(name=cat_name)
            if check.exists():
                cat_id = Category.objects.get(name=cat_name)
                region_name = region_name[:2]
                region_id = Region.objects.get(name=region_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                    filter(region=region_id, category=cat_id)
            else:
                region_name = region_name[:2]
                region_id = Region.objects.get(name=region_name)
                detail_cat_id = DetailCategory.objects.get(detail_name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                    filter(region=region_id, detail_category=detail_cat_id)

        elif re.search(r'전체', region_name) and not (re.search(r'전체', cat_name)):
            region_name = region_name[:2]
            region_id = Region.objects.get(name=region_name)
            sub_cat_id = SubCategory.objects.get(sub_name=cat_name)
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                filter(region=region_id, sub_category=sub_cat_id)

        elif not (re.search(r'전체', region_name)) and re.search(r'전체', cat_name):
            cat_name = cat_name[:-2].strip()
            check = Category.objects.filter(name=cat_name)
            if check.exists():
                detail_region_id = DetailRegion.objects.get(detail_name=region_name)
                cat_id = Category.objects.get(name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                    filter(detail_region=detail_region_id, category=cat_id)

            else:
                detail_region_id = DetailRegion.objects.get(detail_name=region_name)
                detail_cat_id = DetailCategory.objects.get(detail_name=cat_name)
                query_set = User.objects.prefetch_related('user_question'). \
                    annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                    filter(detail_region=detail_region_id, detail_category=detail_cat_id)

        else:
            detail_region_id = DetailRegion.objects.get(detail_name=region_name)
            sub_cat_id = SubCategory.objects.get(sub_name=cat_name)
            query_set = User.objects.prefetch_related('user_question'). \
                annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).\
                filter(detail_region=detail_region_id, sub_category=sub_cat_id)

    serializer = UserSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)


# Create your views here.
@csrf_exempt
def info_list(request, uid):
    query_set = User.objects.prefetch_related('user_question', 'reviewer_question').select_related('sub_category').\
        annotate(total_review=Count('user_question__id'), avg_point=Avg('user_question__point')).filter(uid=uid)
    serializer = InfoSerializer(query_set, many=True)
    return JsonResponse(serializer.data, safe=False)
