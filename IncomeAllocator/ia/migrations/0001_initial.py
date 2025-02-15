# Generated by Django 5.0.4 on 2024-04-21 08:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('income', models.IntegerField(default=0)),
                ('rent', models.IntegerField(default=0)),
                ('transport', models.IntegerField(default=0)),
                ('other', models.IntegerField(default=0)),
                ('entertainment', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
