# Generated by Django 2.2.2 on 2019-07-02 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_data_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='age',
        ),
        migrations.RemoveField(
            model_name='data',
            name='name',
        ),
    ]
