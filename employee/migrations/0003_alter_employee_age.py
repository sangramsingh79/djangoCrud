# Generated by Django 4.2.4 on 2024-06-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Age',
            field=models.BigIntegerField(),
        ),
    ]
