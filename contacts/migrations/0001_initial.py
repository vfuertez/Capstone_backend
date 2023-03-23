# Generated by Django 4.1.7 on 2023-03-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
