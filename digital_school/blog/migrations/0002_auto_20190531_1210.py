# Generated by Django 2.2.1 on 2019-05-31 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('date_posted',)},
        ),
    ]
