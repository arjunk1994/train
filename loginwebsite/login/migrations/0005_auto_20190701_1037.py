# Generated by Django 2.2.2 on 2019-07-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190628_0605'),
    ]

    operations = [
        migrations.DeleteModel(
            name='info',
        ),
        migrations.RemoveField(
            model_name='data',
            name='password',
        ),
        migrations.AddField(
            model_name='data',
            name='emailid',
            field=models.EmailField(default='noemail@arjun.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.TextField(max_length=75),
        ),
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='data',
            name='username',
            field=models.TextField(unique=True),
        ),
    ]
