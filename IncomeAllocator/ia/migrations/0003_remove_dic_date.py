# Generated by Django 5.0.4 on 2024-04-26 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0002_dic_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dic',
            name='date',
        ),
    ]
