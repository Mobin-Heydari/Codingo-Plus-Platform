# Generated by Django 5.2.1 on 2025-06-26 03:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0007_courseticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTicketMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_messages', to='Tickets.courseticket', verbose_name='تیکت دوره')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پیام تیکت دوره',
                'verbose_name_plural': 'پیام\u200c های تیکت دوره',
                'ordering': ['created_at'],
            },
        ),
    ]
