# Generated by Django 2.1.2 on 2018-11-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_test1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
