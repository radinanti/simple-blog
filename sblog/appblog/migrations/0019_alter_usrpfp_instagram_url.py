# Generated by Django 4.2.3 on 2023-09-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0018_usrpfp_instagram_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usrpfp',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]