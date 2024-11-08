# Generated by Django 5.0.2 on 2024-11-08 17:26

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('freelancer', 'Freelancer'), ('viewer', 'Viewer')], default='viewer', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('communication_address', models.TextField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_area', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreelancerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('communication_address', models.TextField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='freelancers_app.freelancerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account', models.CharField(max_length=50)),
                ('gpay_number', models.CharField(blank=True, max_length=15, null=True)),
                ('phonepe_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancers_app.freelancerprofile')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancers_app.task')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_link', models.URLField()),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='task_submissions/')),
                ('description', models.TextField(blank=True, null=True)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='freelancers_app.freelancerprofile')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='freelancers_app.task')),
            ],
        ),
    ]
