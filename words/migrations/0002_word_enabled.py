# Generated by Django 4.0.2 on 2022-02-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]