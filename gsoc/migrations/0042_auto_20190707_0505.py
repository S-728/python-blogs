# Generated by Django 2.1.9 on 2019-07-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("gsoc", "0041_auto_20190707_0432")]

    operations = [
        migrations.AddField(
            model_name="suborgdetails",
            name="created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="suborgdetails",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
