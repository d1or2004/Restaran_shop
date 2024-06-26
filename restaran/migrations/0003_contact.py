# Generated by Django 5.0.4 on 2024-05-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaran', '0002_foodmenu_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
