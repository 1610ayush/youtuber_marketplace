# Generated by Django 4.0.3 on 2022-04-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='to_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
