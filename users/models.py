from django.db import models
from region.models import *
from category.models import *


# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    folder = models.TextField(default="")

    class Meta:
        db_table = 'image'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    intro = models.TextField(default="")
    imageUrl = models.ForeignKey(Image, on_delete=models.CASCADE)

    numberOfEmploy = models.IntegerField(default=0)

    connection_time = models.DateTimeField(auto_now_add=True)

    detail_service = models.TextField(default="")

    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    detail_region = models.ForeignKey(DetailRegion, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    detail_category = models.ForeignKey(DetailCategory, on_delete=models.CASCADE, default="")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = 'users'


class Detail_Image(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.TextField(default="")

    class Meta:
        db_table = 'detail_image'


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.TextField(default="")
    which_info = models.CharField(default="", max_length=2)

    class Meta:
        db_table = 'info'


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.TextField(default="")

    class Meta:
        db_table = 'service'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer_question')
    point = models.IntegerField(default=0)
    Content = models.TextField(default="")
    reviewResponse = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(default="")
    answer = models.TextField(default="")

    class Meta:
        db_table = 'question'