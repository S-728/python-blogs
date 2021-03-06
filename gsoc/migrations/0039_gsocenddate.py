# Generated by Django 2.1.9 on 2019-07-03 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("gsoc", "0038_auto_20190702_0326")]

    operations = [
        migrations.CreateModel(
            name="GsocEndDate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "timeline",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="gsoc.Timeline"
                    ),
                ),
            ],
        )
    ]
