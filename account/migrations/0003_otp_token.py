# Generated by Django 4.2.3 on 2023-07-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_otp"),
    ]

    operations = [
        migrations.AddField(
            model_name="otp",
            name="token",
            field=models.CharField(max_length=111, null=True),
        ),
    ]
