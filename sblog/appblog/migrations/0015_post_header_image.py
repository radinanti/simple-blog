# Generated by Django 4.2.3 on 2023-08-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0014_remove_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='header/'),
        ),
    ]