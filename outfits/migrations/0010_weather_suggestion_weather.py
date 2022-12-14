# Generated by Django 4.1.2 on 2022-11-17 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("outfits", "0009_suggestion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Weather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("dt", models.DateTimeField(max_length=20)),
                ("description", models.CharField(max_length=50)),
                ("temp", models.FloatField()),
                ("temp_min", models.FloatField()),
                ("temp_max", models.FloatField()),
                ("speed", models.FloatField()),
                ("country", models.CharField(max_length=20)),
                ("pressure", models.FloatField()),
                ("humidity", models.FloatField()),
                ("feels_like", models.FloatField()),
                ("icon", models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name="suggestion",
            name="weather",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="outfits.weather",
            ),
            preserve_default=False,
        ),
    ]
