from django.db import models


# Create your models here.


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'region'


class DetailRegion(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.IntegerField(default=0)
    detail_name = models.CharField(max_length=20, blank=False, null=False)


    class Meta:
        db_table = 'detail_region'
