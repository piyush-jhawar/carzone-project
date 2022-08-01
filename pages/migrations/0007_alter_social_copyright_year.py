# Generated by Django 4.0.6 on 2022-07-30 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_social_copyright_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='copyright_year',
            field=models.IntegerField(default=2022, validators=[django.core.validators.MaxLengthValidator(4)]),
        ),
    ]