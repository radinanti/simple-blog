# Generated by Django 4.2.3 on 2023-08-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0005_alter_post_title_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
    ]
