# Generated by Django 4.2.3 on 2023-08-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0017_usrpfp_github_url_usrpfp_profile_usrpfp_twitter_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usrpfp',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
