# Generated by Django 5.1.3 on 2024-12-05 14:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ia', '0003_remove_dic_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dic',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
