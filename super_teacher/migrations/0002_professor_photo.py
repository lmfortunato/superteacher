# Generated by Django 4.2.6 on 2023-11-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='photo',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
