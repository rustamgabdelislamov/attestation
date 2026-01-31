from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите email"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Необязательное поле. Введите номер телефона",
    )
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Необязательное поле. Введите страну",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активность",
        blank=True,
        null=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
