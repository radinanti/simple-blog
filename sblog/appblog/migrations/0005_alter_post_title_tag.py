# Generated by Django 4.2.3 on 2023-08-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0004_rename_text_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]