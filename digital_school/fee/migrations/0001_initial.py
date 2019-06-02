# Generated by Django 2.2.1 on 2019-05-29 18:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='concession_type',
            fields=[
                ('concession_code', models.AutoField(primary_key=True, serialize=False)),
                ('concession_type', models.CharField(max_length=255)),
                ('concession_percent', models.IntegerField(default=50)),
            ],
            options={
                'ordering': ('concession_code',),
            },
        ),
        migrations.CreateModel(
            name='fees_source',
            fields=[
                ('source_code', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('source_code',),
            },
        ),
        migrations.CreateModel(
            name='fees_type',
            fields=[
                ('fee_code', models.AutoField(primary_key=True, serialize=False)),
                ('fee_type', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('fee_code',),
            },
        ),
        migrations.CreateModel(
            name='fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_dues', models.BigIntegerField(default=1000)),
                ('paid', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=1)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('paid_date', models.DateField(default=django.utils.timezone.now)),
                ('Gr_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.gr_register')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Classes')),
                ('fee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fee.fees_type')),
                ('gardian_code', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='student.gardian')),
                ('paid_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fee.fees_source')),
            ],
            options={
                'ordering': ('Gr_num',),
            },
        ),
        migrations.CreateModel(
            name='class_fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_amount', models.BigIntegerField(default=1000)),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Classes')),
                ('fee_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fee.fees_type')),
            ],
            options={
                'ordering': ('class_code',),
            },
        ),
    ]