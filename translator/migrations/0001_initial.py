# Generated by Django 3.2 on 2022-03-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100, verbose_name='English word')),
                ('uzbek', models.CharField(max_length=100, verbose_name='Uzbek word')),
            ],
        ),
    ]