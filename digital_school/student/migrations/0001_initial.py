# Generated by Django 2.2.1 on 2019-05-29 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_code', models.AutoField(primary_key=True, serialize=False)),
                ('area_text', models.CharField(max_length=50, verbose_name='Area Block')),
            ],
            options={
                'ordering': ('area_code',),
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_code', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('class_code',),
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('section_code', models.AutoField(primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('section_code',),
            },
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('session_code', models.AutoField(primary_key=True, serialize=False)),
                ('session_years', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('session_code',),
            },
        ),
        migrations.CreateModel(
            name='gr_register',
            fields=[
                ('gr_no', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_birth', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('FM', 'Female')], max_length=10)),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Home Address')),
                ('status', models.CharField(choices=[('P', 'Present'), ('FM', 'Left')], default='P', max_length=10)),
                ('area_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Area', verbose_name='Area')),
                ('classes_A', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='classes_A', to='student.Classes', verbose_name='Class of Admission')),
                ('classes_C', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes_C', to='student.Classes', verbose_name='Current Class')),
                ('sections_A', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sections_A', to='student.Sections', verbose_name='Section of Admission')),
                ('sections_C', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections_C', to='student.Sections', verbose_name='Current Section')),
            ],
            options={
                'ordering': ('gr_no',),
            },
        ),
        migrations.CreateModel(
            name='gardian',
            fields=[
                ('family_id', models.AutoField(primary_key=True, serialize=False)),
                ('father_name', models.CharField(max_length=50, verbose_name="Father's Name")),
                ('father_profession', models.CharField(max_length=50, verbose_name="Father's Occupation")),
                ('father_cell', models.CharField(max_length=50, verbose_name="Father's Cell Number")),
                ('mother_name', models.CharField(max_length=50, verbose_name="Mother's Name")),
                ('mother_cell', models.CharField(max_length=50, verbose_name="Mother's Cell Number")),
                ('gr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.gr_register')),
            ],
            options={
                'ordering': ('family_id',),
            },
        ),
        migrations.CreateModel(
            name='class_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(null=True, verbose_name='Roll No')),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Classes', verbose_name='Class')),
                ('gr_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.gr_register', verbose_name='Name')),
                ('section_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Sections', verbose_name='Section')),
                ('session_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.session', verbose_name='Session')),
            ],
            options={
                'ordering': ('gr_no',),
            },
        ),
    ]