# Generated by Django 2.0.3 on 2018-03-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('faculty', models.CharField(blank=True, max_length=100, null=True)),
                ('institute', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('enrolled_year', models.IntegerField()),
                ('passed_year', models.IntegerField()),
                ('grade_obtained', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('role', models.TextField()),
                ('start_date', models.CharField(max_length=30)),
                ('end_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('facebook', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quotation', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(choices=[('personal', 'Personal Project'), ('academic', 'Academic Project'), ('commercial', 'Commercial Project')], max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('role', models.TextField()),
                ('description', models.TextField()),
                ('technology_used', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(choices=[('technical', 'Technical Skills'), ('database', 'Database'), ('vcs', 'Versioning Tools'), ('other', 'Other Tools')], max_length=50)),
                ('technology', models.CharField(max_length=100)),
                ('expertise_level', models.CharField(max_length=100)),
            ],
        ),
    ]
