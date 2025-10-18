from django.db import models
from django.contrib.auth.models import User
from jalali_date import date2jalali

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی ها'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts', verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='دسته بندی')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='شناسه یکتا')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True, verbose_name='تصویر')
    published_date = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')
    published_time = models.TimeField(auto_now_add=True, verbose_name='زمان انتشار')
    updated_date = models.DateField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')
    updated_time = models.TimeField(auto_now=True, verbose_name='زمان آخرین ویرایش')

    class Meta:
        ordering = ['-published_date', '-published_time']
        verbose_name = 'نوشته ها'
        verbose_name_plural = 'نوشته ها'
    
    @property
    def published_jalali(self):
        return date2jalali(self.published_date).strftime('%Y/%m/%d')
    
    published_jalali.fget.short_description = 'تاریخ انتشار'
    
    @property
    def updated_jalali(self):
        return date2jalali(self.updated_date).strftime('%Y/%m/%d')
    
    updated_jalali.fget.short_description = 'تاریخ آخرین ویرایش'

    def __str__(self):
        return self.title