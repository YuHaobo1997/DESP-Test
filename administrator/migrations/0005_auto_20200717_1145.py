# Generated by Django 3.0.5 on 2020-07-17 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_auto_20200717_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tabletimeliner',
            options={'managed': True, 'ordering': ['table_timeliner_col_start']},
        ),
    ]
