# Generated by Django 4.2.20 on 2025-04-17 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField(help_text='Comma-separated list of ingredients')),
                ('cooking_time', models.IntegerField(help_text='Cooking time in minutes')),
                ('difficulty', models.CharField(blank=True, max_length=20)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
