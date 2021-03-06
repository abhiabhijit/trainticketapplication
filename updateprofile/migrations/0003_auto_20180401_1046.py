# Generated by Django 2.0.2 on 2018-04-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateprofile', '0002_profile_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_code',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='profile',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name_on_card',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
