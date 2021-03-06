# Generated by Django 4.0.2 on 2022-02-09 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reishop', '0003_category_clothes_is_published_clothes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reishop.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
    ]
