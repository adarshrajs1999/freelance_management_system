# Generated by Django 5.0.2 on 2024-11-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0016_remove_customer_task_is_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('freelancer', 'Freelancer'), ('viewer', 'Viewer')], default='viewer', max_length=10),
        ),
    ]
