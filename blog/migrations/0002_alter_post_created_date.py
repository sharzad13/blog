# Generated by Django 3.2.20 on 2023-08-06 16:26

from django.db import migrations, models
import jdatetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=jdatetime.datetime.now),
        ),
    ]
