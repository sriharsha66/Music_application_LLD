# Generated by Django 5.0.3 on 2024-03-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymp3', '0004_alter_friendrequest_from_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='mymp3.userprofile'),
        ),
    ]
