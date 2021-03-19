from django.db import models


# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, default="")

    class Meta:
        db_table = 'category'


class DetailCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail_name = models.TextField(default="")

    class Meta:
        db_table = 'detail_category'


class SubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    detail_category = models.ForeignKey(DetailCategory, on_delete=models.CASCADE)
    sub_name = models.TextField(default="")

    class Meta:
        db_table = 'sub_category'
