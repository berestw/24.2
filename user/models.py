from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    name = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=30, verbose_name='город', **NULLABLE)
    image = models.ImageField(upload_to='user', verbose_name='изображение', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now_add=True,verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='лекция', **NULLABLE)
    total_sum = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, verbose_name='способ оплаты')

    def __str__(self):
        return f"{self.user} - {self.lesson if self.lesson else self.course}: {self.total_sum}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
