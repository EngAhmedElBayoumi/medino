# Generated by Django 2.2.7 on 2022-06-04 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_ar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book_ar',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
