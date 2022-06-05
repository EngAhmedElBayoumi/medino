# Generated by Django 4.0.5 on 2022-06-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_info_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_ar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=250)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Info',
            },
        ),
    ]
