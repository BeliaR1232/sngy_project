# Generated by Django 3.1.1 on 2020-09-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20200909_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='fire_date',
            field=models.DateField(blank=True, verbose_name='Дата увольнения'),
        ),
    ]