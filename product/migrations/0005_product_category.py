# Generated by Django 4.2.3 on 2023-08-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(blank=True, null=True, to="product.category"),
        ),
    ]
