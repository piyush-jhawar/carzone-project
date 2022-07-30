# Generated by Django 4.0.6 on 2022-07-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_google_plus_link_team_instagram_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='linkedin_link',
            new_name='linkedIn_link',
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
