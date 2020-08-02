# Generated by Django 3.0.8 on 2020-07-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('image_url', models.CharField(max_length=500)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]