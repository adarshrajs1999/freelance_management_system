# Generated by Django 5.0.2 on 2024-11-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0004_alter_task_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_tasks',
            name='payment_amount',
            field=models.CharField(blank=True, null=True),
        ),
    ]
