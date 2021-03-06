# Generated by Django 3.1.1 on 2020-09-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=40, null=True)),
                ('last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=30, null=True)),
                ('birth_place', models.CharField(blank=True, max_length=50, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('languages', models.CharField(blank=True, max_length=100, null=True)),
                ('political_party', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'parliment',
                'managed': True,
            },
        ),
    ]
