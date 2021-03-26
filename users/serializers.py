from abc import ABC

from rest_framework import serializers
from .models import *
from django.db.models import Avg, Max, Min, Sum, Count


class ReviewSimpleSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(read_only=True, source='reviewer')
    description = serializers.CharField(source='Content')

    class Meta:
        model = Review
        fields = (
            'id',
            'reviewer_name',
            'description',
        )


class UserSerializer(serializers.ModelSerializer):
    avg_point = serializers.SerializerMethodField()
    total_review = serializers.SerializerMethodField()
    recent_review = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = (
            'uid',
            'title',
            'imageUrl',
            'intro',
            'avg_point',
            'total_review',
            'numberOfEmploy',
            'recent_review',
            'total',
        )

    def get_recent_review(self, obj: User):
        last_review = obj.user_question.order_by('id').first()
        return ReviewSimpleSerializer(last_review).data

    def get_avg_point(self,obj : User):
        return obj.user_question.values('uid').aggregate(Avg('point'))

    def get_total_review(selfs,obj:User):
        return obj.user_question.values('uid').aggregate(Count('id'))

    def get_total(self, obj : User):
        return User.objects.all().count()


class InfoSimpleSerializer(serializers.ModelSerializer):
    info_title = serializers.CharField(read_only=True, source='info')
    detail_info = serializers.CharField(source='which_info')

    class Meta:
        model = Info
        fields = (
            'info_title',
            'detail_info',
        )


class ServiceSimpleSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(read_only=True, source='service')

    class Meta:
        model = Info
        fields = (
            'service_name',

        )


class Review2SimpleSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(read_only=True, source='reviewer')
    review_point = serializers.IntegerField(read_only=True, source='point')
    review_content = serializers.CharField(read_only=True, source='Content')
    reviewresponse = serializers.CharField(read_only=True, source='reviewResponse')
    review_date = serializers.DateTimeField(read_only=True, source='date')

    class Meta:
        model = Info
        fields = (
            'reviewer_name',
            'review_point',
            'review_content',
            'reviewresponse',
            'review_date',
        )


class QuestionSimpleSerializer(serializers.ModelSerializer):
    question_ = serializers.CharField(read_only=True, source='question')
    answer_ = serializers.CharField(read_only=True, source='answer')

    class Meta:
        model = Info
        fields = (
            'question_',
            'answer_',

        )


class DetailImageSimpleSerializer(serializers.ModelSerializer):
    folder_name = serializers.CharField(read_only=True, source='folder')

    class Meta:
        model = Detail_Image
        fields = (
            'folder_name',
        )


class InfoSerializer(serializers.ModelSerializer):
    avg_point = serializers.FloatField(required=False)
    total_review = serializers.IntegerField(required=False)
    category = serializers.SerializerMethodField()
    detail_info = serializers.SerializerMethodField()
    offer_service = serializers.SerializerMethodField()
    review_info = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'uid',
            'title',
            'imageUrl',
            'category',
            'avg_point',
            'total_review',
            'intro',
            'detail_info',
            'offer_service',
            'detail_service',
            'image',
            'review_info',
            'question',
        )


    def get_image(self, obj: User):
        image = obj.detail_image_set.all()
        return DetailImageSimpleSerializer(image, many=True).data

    def get_category(self, obj: User):
        return obj.sub_category.sub_name

    def get_detail_info(self, obj: User):
        detail_info = obj.info_set.all()
        return InfoSimpleSerializer(detail_info, many=True).data

    def get_offer_service(self, obj: User):
        offer_service = obj.service_set.all()
        return ServiceSimpleSerializer(offer_service, many=True).data

    def get_question(self, obj: User):
        question = obj.question_set.all()
        return QuestionSimpleSerializer(question, many=True).data


    def get_review_info(self, obj: User):
        review_info = obj.user_question.all()
        return Review2SimpleSerializer(review_info, many=True).data