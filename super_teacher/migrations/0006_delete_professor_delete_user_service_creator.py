# Generated by Django 4.2.6 on 2023-11-21 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('super_teacher', '0005_remove_professor_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='service',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
