# Generated by Django 5.2.1 on 2025-06-03 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tickets', '0003_ticketmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='ticket_attachments/', verbose_name='فایل')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپلود')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='Tickets.ticketmessage', verbose_name='پیام')),
            ],
            options={
                'verbose_name': 'پیوست تیکت',
                'verbose_name_plural': 'پیوست\u200c های تیکت',
            },
        ),
    ]
