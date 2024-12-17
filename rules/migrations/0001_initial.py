# Generated by Django 5.1.4 on 2024-12-17 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, help_text='FontAwesome icon class', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('full_text', models.TextField(blank=True, null=True)),
                ('severity', models.CharField(choices=[('low', 'Low Impact'), ('medium', 'Medium Impact'), ('high', 'High Impact'), ('critical', 'Critical')], default='medium', max_length=20)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('active', 'Active'), ('archived', 'Archived')], default='draft', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('applicable_to', models.CharField(default='All', help_text='Who this rule applies to (e.g., Students, Staff, All)', max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_rules', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='rules.rulecategory')),
            ],
        ),
        migrations.CreateModel(
            name='RuleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='rule_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rules.rule')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('evidence', models.FileField(blank=True, null=True, upload_to='violation_evidence/')),
                ('status', models.CharField(choices=[('reported', 'Reported'), ('under_investigation', 'Under Investigation'), ('resolved', 'Resolved'), ('dismissed', 'Dismissed')], default='reported', max_length=30)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('resolved_at', models.DateTimeField(blank=True, null=True)),
                ('offender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rule_violations', to=settings.AUTH_USER_MODEL)),
                ('reported_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_violations', to=settings.AUTH_USER_MODEL)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='violations', to='rules.rule')),
            ],
        ),
    ]
