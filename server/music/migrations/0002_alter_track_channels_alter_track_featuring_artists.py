# Generated by Django 5.1.4 on 2025-01-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='channels',
            field=models.ManyToManyField(blank=True, to='music.channel'),
        ),
        migrations.AlterField(
            model_name='track',
            name='featuring_artists',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
