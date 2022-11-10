# Generated by Django 4.1.2 on 2022-11-04 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='outfits.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=10)),
                ('shade', models.CharField(max_length=10)),
                ('picture', models.CharField(max_length=250)),
                ('weather_value', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.category')),
            ],
        ),
        migrations.CreateModel(
            name='Formality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('F', 'FORMAL'), ('S', 'SEMI-FORMAL'), ('C', 'CASUAL')], max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.product')),
            ],
        ),
    ]