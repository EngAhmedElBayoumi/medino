# Generated by Django 4.0.3 on 2022-04-09 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_create_by_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
