# Generated by Django 4.2 on 2024-12-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_hcui3f', upload_to='images/'),
        ),
    ]