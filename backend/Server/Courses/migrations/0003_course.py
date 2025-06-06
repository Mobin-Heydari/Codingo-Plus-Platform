# Generated by Django 5.2.1 on 2025-06-02 04:45

import ckeditor_uploader.fields
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_subcategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان دوره')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='نامک')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات دوره')),
                ('duration', models.DurationField(default=datetime.timedelta(0), verbose_name='مدت زمان دوره')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='قیمت دوره')),
                ('master_note', models.CharField(blank=True, max_length=200, null=True, verbose_name='یادداشت مدرس')),
                ('payment_status', models.CharField(choices=[('F', 'رایگان'), ('P', 'پولی')], default='P', max_length=10, verbose_name='آیا دوره پولی است یا رایگان؟')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='Courses/posters/', verbose_name='پوستر دوره')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='Courses/banners/', verbose_name='بنر دوره')),
                ('level_status', models.CharField(choices=[('IN', 'مقدماتی'), ('AD', 'پیشرفته'), ('IA', 'مقدماتی تا پیشرفته')], default='IN', max_length=30, verbose_name='سطح دوره')),
                ('course_status', models.CharField(choices=[('C', 'تکمیل شده'), ('I', 'درحال برگزاری'), ('S', 'شروع به زودی')], default='S', max_length=20, verbose_name='وضعیت دوره')),
                ('status', models.CharField(choices=[('DR', 'پیش نویس شود'), ('PD', 'منتشر شود')], default='DR', max_length=10, verbose_name='وضعیت')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='آیا دوره، پیشنهادی است؟')),
                ('views', models.IntegerField(default=0, verbose_name='بازدید ها')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('category', models.ManyToManyField(related_name='courses', to='Courses.subcategory', verbose_name='دسته بندی')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='مدرس دوره')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
    ]
