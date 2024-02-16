# Generated by Django 5.0.1 on 2024-01-03 15:58

import test_tube_yum_yums.models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hb', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('PCV', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('RBC_count', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('MCV', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('MCH', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('MCHC', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('RDW', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('TLC', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('DLC_N', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('DLC_L', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('DLC_M', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('DLC_E', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('DLC_B', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ALC_N', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ALC_L', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ALC_M', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ALC_E', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ALC_B', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('Platelets', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('MPV', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VitMin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B1', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B2', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B3', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B5', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B6', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B7', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B9', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('B12', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('C', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('D', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('E', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('K', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('Ca', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('P', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('Mg', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('Zn', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField()),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('diabetes', models.BooleanField(null=True)),
                ('bp', models.BooleanField(null=True)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('height', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('bmi', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('ast', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('systolic', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('diastolic', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VitMinStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_range', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='vitmin_lower_range', to='test_tube_yum_yums.vitmin')),
                ('upper_range', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='vitmin_upper_range', to='test_tube_yum_yums.vitmin')),
                ('vitmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vitmin_report', to='test_tube_yum_yums.vitmin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vitmin_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbc_lower', models.ForeignKey(default=test_tube_yum_yums.models.CBC.get_low, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cbc_lower', to='test_tube_yum_yums.cbc')),
                ('cbc_upper', models.ForeignKey(default=test_tube_yum_yums.models.CBC.get_high, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cbc_upper', to='test_tube_yum_yums.cbc')),
                ('vitmin_lower', models.ForeignKey(default=test_tube_yum_yums.models.VitMin.get_low, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='vitmin_lower', to='test_tube_yum_yums.vitmin')),
                ('vitmin_upper', models.ForeignKey(default=test_tube_yum_yums.models.VitMin.get_high, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='vitmin_upper', to='test_tube_yum_yums.vitmin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CBCStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cbcc_report', to='test_tube_yum_yums.cbc')),
                ('lower_range', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cbc_lower_range', to='test_tube_yum_yums.cbc')),
                ('upper_range', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cbc_upper_range', to='test_tube_yum_yums.cbc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cbc_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]