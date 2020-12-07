# Generated by Django 3.1.4 on 2020-12-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaktimeapi', '0002_auto_20201031_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(default='', max_length=1)),
                ('manager', models.CharField(max_length=255)),
                ('funding', models.CharField(max_length=255)),
                ('date', models.DateField(default='2019-12-14')),
                ('time_from', models.TimeField(null=True)),
                ('time_to', models.TimeField(null=True)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Shift',
        ),
    ]