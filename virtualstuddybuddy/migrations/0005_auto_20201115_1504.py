# Generated by Django 3.1.1 on 2020-11-15 20:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualstuddybuddy', '0004_auto_20201109_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to answer')], default='', max_length=200, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('African American and African Studies', 'African American and African Studies'), ('American Studies', 'American Studies'), ('Anthropology', 'Anthropology'), ('Archaeology', 'Archaeology'), ('Architectural History', 'Architectural History'), ('Architecture', 'Architecture'), ('Astronomy', 'Astronomy'), ('Bachelor of Interdisciplinary Studies', 'Bachelor of Interdisciplinary Studies'), ('Bachelor of Professional Studies in Health Sciences Management', 'Bachelor of Professional Studies in Health Sciences Management'), ('Biology', 'Biology'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Classics', 'Classics'), ('Cognitive Science', 'Cognitive Science'), ('Commerce', 'Commerce'), ('Comparative Literature', 'Comparative Literature'), ('Computer Engineering', 'Computer Engineering'), ('Computer Science (B.A.)', 'Computer Science (B.A.)'), ('Computer Science (B.S.)', 'Computer Science (B.S.)'), ('Dance', 'Dance'), ('Drama', 'Drama'), ('East Asian Languages, Literatures and Culture', 'East Asian Languages, Literatures and Culture'), ('Economics', 'Economics'), ('Electrical Engineering', 'Electrical Engineering'), ('Engineering Science', 'Engineering Science'), ('English', 'English'), ('Environmental Sciences', 'Environmental Sciences'), ('Environmental Thought and Practice', 'Environmental Thought and Practice'), ('Five-Year Teacher Education Program', 'Five-Year Teacher Education Program'), ('French', 'French'), ('German', 'German'), ('German Studies', 'German Studies'), ('Global Studies', 'Global Studies'), ('Global Sustainability Minor', 'Global Sustainability Minor'), ('Historic Preservation Minor', 'Historic Preservation Minor'), ('History', 'History'), ('History of Art', 'History of Art'), ('Human Biology', 'Human Biology'), ('Interdisciplinary Major of Global Studies', 'Interdisciplinary Major of Global Studies'), ('Jewish Studies', 'Jewish Studies'), ('Kinesiology (BSEd)', 'Kinesiology (BSEd)'), ('Landscape Architecture Minor', 'Landscape Architecture Minor'), ('Latin American Studies', 'Latin American Studies'), ('Linguistics', 'Linguistics'), ('Materials Science and Engineering', 'Materials Science and Engineering'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Media Studies', 'Media Studies'), ('Medieval Studies', 'Medieval Studies'), ('Middle Eastern and South Asian Languages and Cultures', 'Middle Eastern and South Asian Languages and Cultures'), ('Music', 'Music'), ('Neuroscience', 'Neuroscience'), ('Nursing', 'Nursing'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political and Social Thought', 'Political and Social Thought'), ('Political Philosophy, Policy, and Law', 'Political Philosophy, Policy, and Law'), ('Politics', 'Politics'), ('Psychology', 'Psychology'), ('Religious Studies', 'Religious Studies'), ('Slavic Languages and Literatures', 'Slavic Languages and Literatures'), ('Sociology', 'Sociology'), ('Spanish', 'Spanish'), ('Speech Communication Disorders', 'Speech Communication Disorders'), ('Statistics', 'Statistics'), ('Studio Art', 'Studio Art'), ('Systems Engineering', 'Systems Engineering'), ('Urban and Environmental Planning', 'Urban and Environmental Planning'), ('Women, Gender & Sexuality', 'Women, Gender & Sexuality'), ('Youth & Social Innovation (BSEd)', 'Youth & Social Innovation (BSEd)'), ('Other', 'Other')], default='', max_length=200, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(200)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='group_description',
            field=models.CharField(default='', max_length=300, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(2000)]),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='group_name',
            field=models.CharField(default='', max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_username', models.CharField(default='', max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
                ('subject', models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(50)])),
                ('recipient_username', models.CharField(default='', max_length=20, validators=[django.core.validators.MinLengthValidator(3)])),
                ('message', models.CharField(default='', max_length=1000)),
                ('userinbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='virtualstuddybuddy.userinbox')),
            ],
        ),
        migrations.AddField(
            model_name='userinbox',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='virtualstuddybuddy.profile'),
        ),
    ]
