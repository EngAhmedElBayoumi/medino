# Generated by Django 2.2.7 on 2022-06-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illnesses', '0004_illnesses_about_illness_illnesses_protection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illnesses',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='illnesses',
            name='protection',
            field=models.TextField(),
        ),
    ]
