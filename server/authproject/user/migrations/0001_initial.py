# Generated by Django 5.0 on 2023-12-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('user_type', models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], default='S', max_length=1)),
                ('subscribed', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('user_type', models.CharField(choices=[('T', 'Teacher'), ('S', 'Student')], default='S', max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
