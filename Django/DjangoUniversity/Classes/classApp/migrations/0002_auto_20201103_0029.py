# Generated by Django 3.1.3 on 2020-11-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='Course_Number',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]