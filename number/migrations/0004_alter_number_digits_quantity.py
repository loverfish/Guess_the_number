# Generated by Django 3.2 on 2021-04-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0003_alter_number_digits_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='digits_quantity',
            field=models.IntegerField(),
        ),
    ]
