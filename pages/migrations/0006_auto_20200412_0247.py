# Generated by Django 2.2.7 on 2020-04-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200412_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='teamName',
            field=models.ForeignKey(blank=True, on_delete='CASCADE', to='pages.Team'),
        ),
    ]