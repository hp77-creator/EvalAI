# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-16 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0014_rename_job_id_field_in_submission_model_to_job_name")
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="status",
            field=models.CharField(
                choices=[
                    ("submitted", "submitted"),
                    ("running", "running"),
                    ("failed", "failed"),
                    ("cancelled", "cancelled"),
                    ("finished", "finished"),
                    ("submitting", "submitting"),
                    ("archived", "archived"),
                ],
                db_index=True,
                max_length=30,
            ),
        )
    ]