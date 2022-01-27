# Generated by Django 4.0.1 on 2022-01-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cloth_name', models.CharField(max_length=200)),
                ('cloth_brand', models.CharField(max_length=200)),
                ('cloth_size', models.CharField(max_length=200)),
                ('cloth_date_release', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]