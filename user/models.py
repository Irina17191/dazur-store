from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Розширена модель користувача з підтримкою різних типів user(ів)"""

    ADMIN = "admin"
    CUSTOMER = "customer"

    USER_TYPE_CHOICES = [
        (ADMIN, "Admin"),
        (CUSTOMER, "Customer"),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
        verbose_name="User type"
    )


    class Meta:
        ordering = ("username",)


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
