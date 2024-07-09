# Generated by Django 5.0.6 on 2024-06-01 23:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Fecha de publicación"
            ),
        ),
    ]