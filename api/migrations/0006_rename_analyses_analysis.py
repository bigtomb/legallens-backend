# Generated by Django 5.1.4 on 2025-01-05 18:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_rename_analyses_analyses_analysis"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Analyses",
            new_name="Analysis",
        ),
    ]
