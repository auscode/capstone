# Generated by Django 4.1 on 2022-09-12 15:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("ottanime", "0006_alter_movie_age_limit_alter_movie_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="type",
            field=models.CharField(
                choices=[("single", "Single"), ("seasonal", "Seasonal")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="movie",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("3e333764-0d69-42f3-b3a3-44d5d268d3a3")
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("031aaddf-113b-494f-9e60-fd6a4381829e")
            ),
        ),
    ]
