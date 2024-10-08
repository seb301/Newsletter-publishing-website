# Generated by Django 5.0.6 on 2024-06-14 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptCode', models.CharField(max_length=5)),
                ('deptName', models.CharField(max_length=100)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='News_volume_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
                ('issue', models.IntegerField()),
                ('month_year', models.DateField(null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('deptId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news_app.department')),
            ],
        ),
    ]
