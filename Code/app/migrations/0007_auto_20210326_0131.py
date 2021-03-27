# Generated by Django 2.2.10 on 2021-03-25 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_student_data_source_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='data_source_id',
        ),
        migrations.AddField(
            model_name='student',
            name='data_source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Data_source'),
        ),
    ]