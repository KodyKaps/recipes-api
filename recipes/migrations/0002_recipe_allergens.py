# Generated by Django 4.2.20 on 2025-04-17 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='allergens',
            field=models.TextField(null=True),
        ),
    ]
