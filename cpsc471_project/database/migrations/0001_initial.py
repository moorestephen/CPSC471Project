# Generated by Django 5.0.4 on 2024-04-13 17:47

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
            name='Club',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sanctioned', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
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
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Coach'), (3, 'Swimmer')], null=True)),
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
            name='Admin',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('tenure_start', models.DateField()),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.club')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('tenure_start', models.DateField()),
                ('contract_start', models.DateField()),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=30)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.club')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionCoachDelegations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.coach')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.competition')),
                ('delegating_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.PositiveIntegerField()),
                ('stroke', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=20)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.competition')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('monthly_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.club')),
            ],
        ),
        migrations.CreateModel(
            name='GroupCoaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.coach')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupPractices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.group')),
            ],
        ),
        migrations.CreateModel(
            name='Swimmer',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=30)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.club')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.TimeField()),
                ('final_time_seconds', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
                ('stroke', models.CharField(max_length=30)),
                ('course', models.CharField(max_length=20)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.competition')),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.swimmer')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.TimeField()),
                ('final_time', models.PositiveIntegerField()),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.swimmer')),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionSwimmersAttending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.competition')),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.swimmer')),
            ],
        ),
        migrations.CreateModel(
            name='SwimmerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.group')),
                ('swimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.swimmer')),
            ],
        ),
    ]
