# Generated by Django 2.2.6 on 2019-11-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payingGuestApp', '0002_auto_20191103_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payingguestdetails',
            name='ac_no_ac',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payingguestdetails',
            name='male_or_female',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payingguestdetails',
            name='wifi_no_wifi',
            field=models.IntegerField(max_length=100),
        ),
    ]