# Generated by Django 3.2 on 2021-04-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MushroomXpert_main', '0002_auto_20210414_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushroom',
            name='id',
        ),
        migrations.AlterField(
            model_name='mushroom',
            name='name',
            field=models.CharField(default='none', max_length=30, primary_key=True, serialize=False),
        ),
    ]
