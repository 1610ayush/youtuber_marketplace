# Generated by Django 4.0.3 on 2022-04-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_team_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(max_length=250),
        ),
    ]