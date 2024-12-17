# Generated by Django 5.1.1 on 2024-11-25 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_start', models.DateField()),
                ('year_end', models.DateField()),
                ('description', models.CharField(help_text='Example: 2024-2025 Academic Year', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_number', models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('holiday_date', models.DateField()),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holidays', to='academic_calendar.academicyear')),
            ],
            options={
                'ordering': ['holiday_date'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_date', models.DateField()),
                ('is_holiday', models.BooleanField(default=False)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='academic_calendar.semester')),
            ],
            options={
                'ordering': ['event_date'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terms', to='academic_calendar.academicyear')),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='academic_calendar.term'),
        ),
    ]
