# Generated by Django 4.1.2 on 2022-11-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug_field',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
