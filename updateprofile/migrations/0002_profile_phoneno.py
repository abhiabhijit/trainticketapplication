# Generated by Django 2.0.2 on 2018-03-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phoneno',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
