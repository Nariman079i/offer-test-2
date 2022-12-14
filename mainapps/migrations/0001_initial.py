# Generated by Django 4.1.2 on 2022-11-02 01:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('priority', models.IntegerField(help_text='Priority integer from 1 to 10', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Priority')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name for Application', max_length=30, verbose_name='Name')),
                ('article', models.IntegerField(help_text='Article for Application', verbose_name='Article')),
                ('file', models.FileField(upload_to='appfiles')),
                ('size', models.FloatField(help_text='Detected automatically', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(24.0)], verbose_name='Size')),
                ('role_id', models.ForeignKey(help_text='Select is Role', on_delete=django.db.models.deletion.CASCADE, to='mainapps.role', verbose_name='Role')),
            ],
        ),
    ]
