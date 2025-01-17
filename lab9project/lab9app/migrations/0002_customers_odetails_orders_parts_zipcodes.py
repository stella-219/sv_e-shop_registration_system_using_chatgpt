# Generated by Django 5.1.2 on 2024-11-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lab9app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customers",
            fields=[
                ("cno", models.IntegerField(primary_key=True, serialize=False)),
                ("cname", models.CharField(blank=True, max_length=18, null=True)),
                ("street", models.CharField(blank=True, max_length=30, null=True)),
                ("zip", models.CharField(blank=True, max_length=6, null=True)),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                "db_table": "customers",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Odetails",
            fields=[
                ("ono", models.IntegerField(primary_key=True, serialize=False)),
                ("pno", models.IntegerField(blank=True, null=True)),
                ("qty", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "odetails",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("ono", models.IntegerField(primary_key=True, serialize=False)),
                ("cno", models.IntegerField(blank=True, null=True)),
                ("eno", models.IntegerField(blank=True, null=True)),
                ("received", models.DateField(blank=True, null=True)),
                ("shipped", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": "orders",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Parts",
            fields=[
                ("pno", models.IntegerField(primary_key=True, serialize=False)),
                ("pname", models.CharField(blank=True, max_length=30, null=True)),
                ("qoh", models.IntegerField(blank=True, null=True)),
                (
                    "prices",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                ("wlevel", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "parts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Zipcodes",
            fields=[
                (
                    "zip",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("city", models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                "db_table": "zipcodes",
                "managed": False,
            },
        ),
    ]
