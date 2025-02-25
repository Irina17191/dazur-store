# Generated by Django 5.1.5 on 2025-02-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price_usd",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
