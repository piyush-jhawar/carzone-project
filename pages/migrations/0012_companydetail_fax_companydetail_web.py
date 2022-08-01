# Generated by Django 4.0.6 on 2022-07-31 05:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_companydetail_copyright_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetail',
            name='fax',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AddField(
            model_name='companydetail',
            name='web',
            field=models.EmailField(default='test@test.com', max_length=254, unique=True),
        ),
    ]