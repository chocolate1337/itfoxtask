# Generated by Django 3.2.3 on 2021-05-13 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210513_2342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
    ]
