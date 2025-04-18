# Generated by Django 5.1.4 on 2025-01-25 04:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0011_coursematerial_external_url_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SearchLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("query", models.CharField(max_length=255)),
                ("results_count", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("filters_applied", models.JSONField(blank=True, default=dict)),
                (
                    "search_type",
                    models.CharField(
                        choices=[
                            ("course", "Course Search"),
                            ("material", "Material Search"),
                            ("forum", "Forum Search"),
                        ],
                        default="course",
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
