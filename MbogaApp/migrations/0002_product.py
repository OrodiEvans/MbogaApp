# Generated by Django 4.2.7 on 2023-11-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MbogaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]