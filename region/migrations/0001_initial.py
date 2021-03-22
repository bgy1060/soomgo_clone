# Generated by Django 3.1.7 on 2021-03-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailRegion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('region', models.IntegerField(default=0)),
                ('detail_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'detail_region',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'region',
            },
        ),
    ]
