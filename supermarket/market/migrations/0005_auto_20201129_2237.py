# Generated by Django 3.1.3 on 2020-11-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20201129_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
