# Generated by Django 4.2.4 on 2024-06-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=2)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
