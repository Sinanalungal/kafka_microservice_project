# Generated by Django 5.0.3 on 2024-03-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
