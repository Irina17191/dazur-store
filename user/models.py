from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CustomUser(AbstractUser):
    """Розширена модель користувача з підтримкою різних типів user(ів)"""

    ADMIN = "admin"
    CUSTOMER = "customer"

    USER_TYPE_CHOICES = [
        (ADMIN, "Admin"),
        (CUSTOMER, "Customer"),
    ]

    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message="Age cannot be less than 2 years old"),
            MaxValueValidator(100, message="Age cannot be more than 100 years old")
        ],
        verbose_name="age",
        help_text="Please indicate your age (optional)",
        blank=True,    # Дозволяє залишати поле порожнім у формах
        null=True      # Дозволяє зберігати NULL у базі даних
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
        verbose_name="User type"
    )


    class Meta:
        ordering = ("username",)


    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


    def is_admin(self):
        """Перевіряє, чи є користувач адміністратором"""
        return self.user_type == self.ADMIN


    def is_customer(self):
        """Перевіряє, чи є користувач покупцем"""
        return self.user_type == self.CUSTOMER


# credentials for superuser
# python manage.py createsuperuser
# Username: admin
# Email address: irynahoncharenko9@gmail.com
# Password: nw2Q4D4D
# Superuser created successfully.
