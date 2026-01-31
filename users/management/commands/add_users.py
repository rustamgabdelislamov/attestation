from django.core.management import BaseCommand

from electronics.models import Contact, Product, Organization
from users.models import CustomUser


class Command(BaseCommand):
    help = "Создаем 3 пользователей и реферальные ссылки"

    def handle(self, *args, **options):
        users = []

        users_data = [
            {
                "email": "fact@mail.ru",
                "password": "password123",
            },
            {"email": "com@mail.ru", "password": "password123", "is_active": "False"},
        ]

        for user_data in users_data:
            # Удаляем пароль из данных пользователя, если он есть
            password = user_data.pop("password", None)

            # Получаем или создаем пользователя
            user, created = CustomUser.objects.get_or_create(**user_data)

            # Если пользователь был создан, устанавливаем хэшированный пароль
            if created:
                if password:
                    user.set_password(password)  # Хэшируем пароль
                    user.save()  # Сохраняем изменения в базе данных
                self.stdout.write(self.style.SUCCESS(f"Добавили: {user.email}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Пользователь существует: {user.email}")
                )

            users.append(user)

        contacts_data = [
            {
                "email": "factory@mail.ru",
                "country": "Россия",
                "city": "Ufa",
                "street": "USSR",
                "house_number": "70",
            },
            {
                "email": "company@mail.ru",
                "country": "Белорусь",
                "city": "Dyurtyuli",
                "street": "Musina",
                "house_number": "1",
            },
            {
                "email": "rustik_capitalnyi_krasavchik@mail.ru",
                "country": "Казахстан",
                "city": "Dyurtyuli",
                "street": "Lenina",
                "house_number": "40",
            },
        ]
        contacts = []

        for contact_data in contacts_data:
            contact, created = Contact.objects.get_or_create(**contact_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Создали контакт: {contact.email}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Не создали: {contact.email}"))
            contacts.append(contact)

        products = []
        products_data = [
            {"name": "Infinix 20", "model": "126 GB", "release_date": "2025-05-12"},
            {"name": "Samsung", "model": "126 GB", "release_date": "2020-05-12"},
            {"name": "Nokia", "model": "126 GB", "release_date": "2022-05-10"},
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Создали : {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Не создали: {product.name}"))
            products.append(product)

        product_ids = [product.id for product in products]

        organization1, created1 = Organization.objects.get_or_create(
            name="Factory", contact=contacts[0], debt_to_supplier=0
        )
        organization1.products.set(product_ids)
        if created1:
            self.stdout.write(self.style.SUCCESS(f"Создали : {organization1.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Не создали: {organization1.name}"))

        organization2, created2 = Organization.objects.get_or_create(
            name="Company",
            contact=contacts[1],
            supplier=organization1,
            debt_to_supplier=10000,
        )

        organization2.products.set(product_ids)
        if created1:
            self.stdout.write(self.style.SUCCESS(f"Создали : {organization2.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Не создали: {organization2.name}"))

        organization3, created3 = Organization.objects.get_or_create(
            name="IP",
            contact=contacts[2],
            supplier=organization2,
            debt_to_supplier=12000,
        )

        organization3.products.set(product_ids)
        if created1:
            self.stdout.write(self.style.SUCCESS(f"Создали : {organization3.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Не создали: {organization3.name}"))
