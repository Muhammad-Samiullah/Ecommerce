# Generated by Django 3.0.8 on 2020-08-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200801_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customerFirstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='customerLastName',
            field=models.CharField(max_length=50),
        ),
    ]
