from django.db import models
from django.core.exceptions import ValidationError
from Users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from Courses.models import Course


class Coupon(models.Model):
    class TypeStatusChoices(models.TextChoices):
        EXPIRED = 'EX', 'منقضی شده'
        USED = 'US', 'استفاده شده'
        UNUSED = 'UN', 'استفاده نشده'
    
    code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='کد تخفیف'
    )
    discount_value = models.IntegerField(
        verbose_name='مقدار تخفیف (درصد)',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    max_usage = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='حداکثر استفاده'
    )
    usage_count = models.IntegerField(
        default=0,
        verbose_name='تعداد استفاده شده'
    )
    valid_from = models.DateTimeField(
        default=timezone.now,
        verbose_name='معتبر از'
    )
    valid_to = models.DateTimeField(
        verbose_name='معتبر تا'
    )
    type_status = models.CharField(
        max_length=2,
        choices=TypeStatusChoices.choices,
        default=TypeStatusChoices.UNUSED,
        verbose_name='وضعیت کد'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='کاربر اختصاصی',
        help_text='اگر خالی باشد، کد برای همه کاربران معتبر است'
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name='فعال'
    )

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد ‌های تخفیف'

    def __str__(self):
        return self.code

    def is_valid(self, user=None):
        now = timezone.now()

        if now > self.valid_to:
            self.is_active = False
            self.type_status = self.TypeStatusChoices.EXPIRED
            self.save()
            return False
        
        if self.user and self.user != user:
            return False
        
        if self.max_usage and self.usage_count >= self.max_usage:
            self.is_active = False
            self.type_status = self.TypeStatusChoices.USED
            self.save()
            return False
        
        if not self.is_active:
            return False
        
        return True

    def use(self, user=None):
        is_valid, message = self.is_valid(user)
        if not is_valid:
            raise ValidationError(message)
        
        self.usage_count += 1
        
        if self.max_usage and self.usage_count >= self.max_usage:
            self.is_active = False
            self.type_status = self.TypeStatusChoices.USED
        
        self.save()
        return True


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='کاربر'
    )
    coupon = models.ForeignKey(
        Coupon,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='کوپن تخفیف'
    )
    coupon_discount = models.IntegerField(
        default=0,
        verbose_name='مقدار تخفیف اعمال شده'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ به‌روزرسانی'
    )
    
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return f"سبد خرید {self.user.username}"

    @property
    def total_price(self):
        return sum(item.price for item in self.course_items.all())

    @property
    def final_price(self):
        total = self.total_price
        if self.coupon and self.coupon.is_valid(self.user):
            discount = (total * self.coupon.discount_value) / 100
            return total - discount
        return total


class CourseItem(models.Model):
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE, 
        related_name='course_items',
        verbose_name='سبد خرید'
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        verbose_name='دوره'
    )
    price = models.PositiveIntegerField(
        verbose_name='قیمت دوره',
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='تاریخ ایجاد'
    )
    
    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم های سبد خرید'
        unique_together = ('cart', 'course')

    def __str__(self):
        return f'{self.course.title} در سبد {self.cart.user.username}'

    def save(self, *args, **kwargs):
        if not self.price or self.price == 0:
            self.price = self.course.price if self.course.price else 0
        super().save(*args, **kwargs)
