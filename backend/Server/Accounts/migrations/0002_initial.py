# Generated by Django 5.2.1 on 2025-07-17 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='accountresetpassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reset_passwords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercourseenrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_activated_course', to='Courses.course'),
        ),
        migrations.AddField(
            model_name='usercourseenrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_activated_course', to=settings.AUTH_USER_MODEL),
        ),
    ]
