# Generated by Django 3.1.1 on 2020-09-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20200909_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='fire_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата увольнения'),
        ),
    ]