# Generated by Django 4.0.3 on 2022-04-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(default='https:://youtube.com', max_length=250),
        ),
    ]
