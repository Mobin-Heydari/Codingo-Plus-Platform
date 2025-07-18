# Generated by Django 5.2.1 on 2025-07-17 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='adminprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AddField(
            model_name='supporterprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='supporter_profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
