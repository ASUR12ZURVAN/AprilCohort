# Generated by Django 5.1.5 on 2025-04-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caller_number', models.CharField(max_length=40)),
                ('call_duration', models.TimeField()),
                ('call_instance', models.DateTimeField()),
                ('avg_sentiment', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=40)),
            ],
        ),
    ]
