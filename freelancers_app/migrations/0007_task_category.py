# Generated by Django 5.0.2 on 2024-11-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0006_alter_customer_tasks_is_approved_taskapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default='Category not specified', max_length=200),
        ),
    ]
