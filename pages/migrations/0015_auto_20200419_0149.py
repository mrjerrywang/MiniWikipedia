# Generated by Django 2.2.7 on 2020-04-19 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20200419_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='times',
            field=models.DateField(),
        ),
    ]