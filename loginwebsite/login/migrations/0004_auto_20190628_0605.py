# Generated by Django 2.2.2 on 2019-06-28 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190628_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.TextField(max_length=75, null=True),
        ),
    ]