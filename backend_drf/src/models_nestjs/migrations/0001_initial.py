# Generated by Django 4.2.4 on 2023-08-21 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.UUIDField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=200)),
                ('email', models.EmailField(db_column='email', max_length=100, unique=True)),
                ('phone_number', models.CharField(db_column='phone_number', max_length=16, unique=True)),
                ('address', models.CharField(db_column='address', max_length=300)),
                ('password', models.CharField(db_column='password', max_length=128)),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('is_superuser', models.BooleanField(db_column='is_superuser')),
                ('at_created', models.DateTimeField(db_column='at_created')),
                ('last_login', models.DateTimeField(db_column='last_login', null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'provinces',
                'db_table': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('province_id', models.ForeignKey(db_column='province_id', on_delete=django.db.models.deletion.DO_NOTHING, to='models_nestjs.provinces')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'db_table': 'cities',
            },
        ),
    ]