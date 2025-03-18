# Generated by Django 4.1.5 on 2023-03-25 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0005_fitnesstrainer_fitness_vstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=111)),
                ('package_details', models.CharField(max_length=111)),
                ('package_duration', models.CharField(max_length=111)),
                ('package_fees', models.CharField(max_length=111)),
                ('trainer_photo', models.FileField(upload_to='tpackagedocs/')),
                ('fitnesstrainer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.fitnesstrainer')),
                ('yogatrainer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.yogatrainer')),
                ('zumbatrainer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.zumbatrainer')),
            ],
        ),
    ]
