# Generated by Django 4.1.5 on 2023-03-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.FileField(upload_to='fitnessdocs/')),
                ('product_details', models.CharField(max_length=100)),
                ('product_rate', models.CharField(max_length=100)),
                ('product_brand', models.CharField(max_length=100)),
            ],
        ),
    ]
