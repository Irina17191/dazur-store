from django.db import models
from django.utils.text import slugify

# ще створю нові apps: User, Revies, Cart, Payments?


class Category(models.Model):
    """
    Категорія товарів (наприклад: комплект з 2х одиниць, копмлект з 3х одиниць,
    бра, трусики, пояс, гартери)
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        unique=True, blank=True
    )  # blank=True, щоб дозволити авто-генерацію

    def save(self, *args, **kwargs):
        if not self.slug:  # Якщо slug ще не заданий
            self.slug = slugify(self.name)  # Автоматично створює slug з name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"  # Щоб в адмінці множина писалась правильно


class Color(models.Model):
    """Колір товару"""

    name = models.CharField(max_length=100, unique=True)
    hex_code = models.CharField(
        max_length=7, unique=True, help_text="Hex-код кольору (наприклад, #FF5733)"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """Опис товару"""

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # blank=True – дозволяє залишати поле порожнім у формах Django (наприклад, у Django Admin)
    # null=True – дозволяє зберігати NULL у базі даних
    # image = models.ImageField(upload_to="products/")
    description = models.TextField()
    material = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color, related_name="products")
    available = models.BooleanField(default=True)  # True = YES, False = SOLD OUT

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}   price: {self.price}"

    def get_available_display(self):
        """Повертає гарний текст для відображення в шаблонах"""
        return "SOLD OUT" if not self.available else "YES"
