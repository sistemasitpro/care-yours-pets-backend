# Generated by Django 4.2.4 on 2023-08-18 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import veterinaries.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('models_nestjs', '__first__'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinaries',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nif_cif', models.CharField(db_column='nif_cif', max_length=10, unique=True)),
                ('name', models.CharField(db_column='name', max_length=200, unique=True)),
                ('description', models.TextField(db_column='description')),
                ('address', models.CharField(db_column='address', max_length=300, unique=True)),
                ('email', models.EmailField(db_column='email', max_length=100, unique=True)),
                ('phone_number', models.CharField(db_column='phone_number', max_length=16, unique=True)),
                ('password', models.CharField(db_column='password', max_length=128)),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False, serialize=False)),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default=False, serialize=False)),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='date_joined', serialize=False)),
                ('last_login', models.DateTimeField(blank=True, db_column='last_login', null=True, serialize=False)),
                ('city_id', models.ForeignKey(db_column='city_id', on_delete=django.db.models.deletion.DO_NOTHING, to='models_nestjs.cities')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'veterinary',
                'verbose_name_plural': 'veterinaries',
                'db_table': 'veterinaries',
            },
            managers=[
                ('objects', veterinaries.models.VeterinaryManager()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategories',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('description', models.CharField(db_column='description', max_length=500)),
            ],
            options={
                'verbose_name': 'service_category',
                'verbose_name_plural': 'service_categories',
                'db_table': 'service_categories',
            },
        ),
        migrations.CreateModel(
            name='VeterinaryService',
            fields=[
                ('uid', models.UUIDField(db_column='uid', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('service_name', models.CharField(db_column='service_name', max_length=200)),
                ('price', models.DecimalField(db_column='price', decimal_places=2, max_digits=6)),
                ('service_category', models.ForeignKey(db_column='service_category', on_delete=django.db.models.deletion.DO_NOTHING, to='veterinaries.servicecategories')),
                ('veterinary_id', models.ForeignKey(db_column='veterinary_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'veterinary_service',
                'verbose_name_plural': 'veterinary_services',
                'db_table': 'veterinary_service',
            },
        ),
    ]