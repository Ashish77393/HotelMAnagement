# Generated by Django 4.2.19 on 2025-04-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('header', models.CharField(max_length=200)),
                ('des', models.CharField(max_length=400)),
            ],
        ),
    ]
