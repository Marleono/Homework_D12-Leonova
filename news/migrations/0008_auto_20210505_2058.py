# Generated by Django 3.1.7 on 2021-05-05 17:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_auto_20210505_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL),
        ),
    ]
