# Generated by Django 5.0.4 on 2024-08-13 21:16

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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('doctype', models.CharField(choices=[('pdf', 'pdf'), ('doc', 'doc'), ('docx', 'docx')], max_length=10)),
                ('keywords', models.CharField(max_length=200)),
                ('project_level', models.CharField(choices=[('nce/nd', 'NCE/ND'), ('hnd', 'HND'), ('ug', 'UNDERGRADUATE'), ('pg', 'POSTGRADUATE')], max_length=16)),
                ('project_type', models.CharField(choices=[('research', 'Research'), ('publication', 'Publication'), ('thesis', 'Thesis'), ('design', 'Design'), ('other', 'Other')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('abstract', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchpro.department')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('exprerience', models.CharField(choices=[('entry', 'Entry'), ('experienced', 'Experienced'), ('expert', 'Expert'), ('master', 'Master'), ('doctor', 'Doctor')], max_length=16)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=16)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchpro.department')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HireWriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_topic', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('cancelled', 'Cancelled'), ('pending', 'Pending')], max_length=16)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchpro.writer')),
            ],
        ),
    ]
