# Generated by Django 4.2.3 on 2023-08-04 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0003_rename_body_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='body',
        ),
    ]