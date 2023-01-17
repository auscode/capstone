# Generated by Django 4.1 on 2023-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ottanime", "0013_alter_movie_age_limit_alter_profile_age_limit"),
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
            model_name="profile",
            name="age_limit",
            field=models.CharField(
                choices=[("kids", "kids"), ("All", "All")], max_length=10
            ),
        ),
    ]
