# Generated by Django 2.0.2 on 2018-03-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_sheetmember_solve_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheetmember',
            name='solve_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]