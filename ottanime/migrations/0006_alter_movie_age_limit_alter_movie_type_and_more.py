# Generated by Django 4.1 on 2022-09-12 14:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("ottanime", "0005_alter_movie_age_limit_alter_movie_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="age_limit",
            field=models.CharField(
                choices=[("kids", "kids"), ("All", "All")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="type",
            field=models.CharField(
                choices=[("seasonal", "Seasonal"), ("single", "Single")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("8f71b194-b429-4be1-84a0-2dc2ac7771ff")
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="age_limit",
            field=models.CharField(
                choices=[("kids", "kids"), ("All", "All")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("d289b784-04f9-4ac2-9d48-bade58d3cb83")
            ),
        ),
    ]
