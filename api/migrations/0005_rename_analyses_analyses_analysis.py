# Generated by Django 5.1.4 on 2025-01-05 17:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_rename_key_points_analyses_analyses_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="analyses",
            old_name="analyses",
            new_name="analysis",
        ),
    ]
