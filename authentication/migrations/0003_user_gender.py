# Generated by Django 4.1.2 on 2022-11-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_alter_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(default="", max_length=1),
        ),
    ]
