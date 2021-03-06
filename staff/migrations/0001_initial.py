# Generated by Django 3.1.1 on 2020-09-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('company_name', models.CharField(max_length=100, verbose_name='Компания')),
                ('position_name', models.CharField(max_length=100, verbose_name='Должность')),
                ('hire_date', models.DateField(verbose_name='Дата приёма')),
                ('fire_date', models.DateField(verbose_name='Дата увольнения')),
                ('salary', models.IntegerField(verbose_name='Ставка')),
                ('fraction', models.IntegerField(verbose_name='Ставка в %')),
                ('base', models.IntegerField(verbose_name='База')),
                ('advance', models.IntegerField(verbose_name='Аванс')),
                ('by_hours', models.BooleanField(default=False, verbose_name='Почасовая оплата')),
            ],
        ),
    ]
