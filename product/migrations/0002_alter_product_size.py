# Generated by Django 4.2.3 on 2023-07-31 06:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.ManyToManyField(
                blank=True, related_name="products", to="product.size"
            ),
        ),
    ]
