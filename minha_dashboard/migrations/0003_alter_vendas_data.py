# Generated by Django 4.1.7 on 2023-05-09 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0002_alter_vendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 14, 41, 6, 433709)),
        ),
    ]
