# Generated by Django 4.0.2 on 2022-11-01 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]