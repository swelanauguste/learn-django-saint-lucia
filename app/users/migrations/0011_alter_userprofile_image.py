# Generated by Django 4.0.1 on 2022-01-23 20:59

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format='JPEG', keep_meta=True, null=True, quality=75, size=[500, 300], upload_to='profile_images'),
        ),
    ]
