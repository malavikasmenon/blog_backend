# Generated by Django 4.1.2 on 2022-11-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='year_of_release',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
