from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Дом")

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers",
        verbose_name="Поставщик",
        help_text="Введите поставщика. Если поставщик не указан, данная организация автоматически считается заводом.",
    )
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_hierarchy_level(self):
        level = 0
        current_obj = self
        while current_obj.supplier is not None:
            current_obj = current_obj.supplier
            level += 1
        return level

    def __str__(self):
        return self.name
