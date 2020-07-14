# Generated by Django 3.0.5 on 2020-07-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_tablequestioncontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableTimeliner',
            fields=[
                ('table_timeliner_col_id', models.AutoField(db_column='Table_Timeliner_col_id', primary_key=True, serialize=False)),
                ('table_timeliner_col_start', models.DateField(db_column='Table_Timeliner_col_start')),
                ('table_timeliner_col_content', models.CharField(db_column='Table_Timeliner_col_content', max_length=255, unique=True)),
                ('table_timeliner_col_end', models.DateField(db_column='Table_Timeliner_col_end')),
                ('table_timeliner_col_status', models.CharField(db_column='Table_Timeliner_col_status', max_length=128)),
                ('table_timeliner_col_name', models.CharField(db_column='Table_Timeliner_col_name', max_length=128)),
                ('table_timeliner_col_evaluation', models.CharField(db_column='Table_Timeliner_col_evaluation', max_length=128)),
            ],
            options={
                'db_table': 'Table_Timeliner',
                'ordering': ['table_timeliner_col_start', 'table_timeliner_col_evaluation'],
                'managed': True,
            },
        ),
    ]
