# Generated by Django 2.2.2 on 2019-07-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20190702_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.TextField(default='yet to enter', max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.TextField(default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='mobile',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.TextField(default='yet to enter', max_length=25, null=True),
        ),
    ]
