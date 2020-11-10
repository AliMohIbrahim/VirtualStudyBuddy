# Generated by Django 3.1.1 on 2020-11-10 02:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualstuddybuddy', '0003_auto_20201105_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='classOf',
            field=models.IntegerField(default=2023, validators=[django.core.validators.MinValueValidator(2020), django.core.validators.MaxValueValidator(2024)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='coursework',
            field=models.CharField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(2000)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(2000)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=200, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(default='', max_length=200, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='uploads/', validators=[django.core.validators.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='New Group', max_length=50)),
                ('group_description', models.CharField(default='Study Group', max_length=300)),
                ('profiles', models.ManyToManyField(to='virtualstuddybuddy.Profile')),
            ],
        ),
    ]