from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from electronics.models import Contact, Product, Organization
from users.models import CustomUser


class ContactTestCase(APITestCase):

    def setUp(self):
        """Тест CRUD для модели Contact если у пользователя is_active=True"""
        self.user = CustomUser.objects.create(email="test@mail.ru", password=1990)
        self.contact = Contact.objects.create(
            email="hrustam911@mail.ru",
            country="Россия",
            city="Дюртюли",
            street="Ленина",
            house_number=40
        )
        self.client.force_authenticate(user=self.user)


    def test_contact_retrieve(self):
        url = reverse("electronics:contacts-detail", args=[self.contact.id])  # Используйте имя URL, сгенерированное router
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.contact.email)

    def test_contact_create(self):
        url = reverse("electronics:contacts-list")
        data = {
            "email": "911@mail.ru",
            "country": "Россия",
            "city": "Дюртюли",
            "street": "Ленина",
            "house_number": 40
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.all().count(), 2)

    def test_contact_update(self):
        url = reverse("electronics:contacts-detail", args=(self.contact.id,))
        data = {
            "city": "Уфа",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("city"), "Уфа")

    def test_contact_delete(self):
        url = reverse("electronics:contacts-detail", args=(self.contact.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.all().count(), 0)

    def test_contact_list(self):
        url = reverse("electronics:contacts-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        result = [
    {
        "id": 1,
        "email": "hrustam911@mail.ru",
        "country": "Россия",
        "city": "Дюртюли",
        "street": "Ленина",
        "house_number": "40"
    }]
        self.assertEqual(data, result)

    def test_is_active_false(self):
        """Тест когда у пользователя is_active=False его не пустит к API"""
        self.false_user = CustomUser.objects.create(email="false@mail.ru", password="password", is_active=False)
        self.client.force_authenticate(user=self.false_user)
        url = reverse("electronics:contacts-detail", args=[self.contact.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProductTestCase(APITestCase):

    def setUp(self):
        """Тест CRUD для модели Product если у пользователя is_active=True"""
        self.user = CustomUser.objects.create(email="test@mail.ru", password=1990)
        self.product = Product.objects.create(
            name="Test",
            model="Test",
            release_date="2026-01-31"
        )
        self.client.force_authenticate(user=self.user)


    def test_product_retrieve(self):
        url = reverse("electronics:products-detail", args=[self.product.id])  # Используйте имя URL, сгенерированное router
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("model"), self.product.model)

    def test_product_create(self):
        url = reverse("electronics:products-list")
        data = {
            "name": "Test2",
            "model": "Test2",
            "release_date": "2026-01-31"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_update(self):
        url = reverse("electronics:products-detail", args=(self.product.id,))
        data = {
            "model": "Test3",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("model"), "Test3")

    def test_product_delete(self):
        url = reverse("electronics:products-detail", args=(self.product.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)

    def test_product_list(self):
        url = reverse("electronics:products-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        result = [
    {
        "id": 1,
        "name": "Test",
        "model": "Test",
        "release_date": "2026-01-31"
    }]
        self.assertEqual(data, result)

class OrganizationTestCase(APITestCase):

    def setUp(self):
        """Тест CRUD для модели Organization если у пользователя is_active=True"""
        self.user = CustomUser.objects.create(email="test@mail.ru", password=1990)
        self.contact = Contact.objects.create(
            email="hrustam911@mail.ru",
            country="Россия",
            city="Дюртюли",
            street="Ленина",
            house_number=40
        )
        self.product = Product.objects.create(
            name="Test",
            model="Test",
            release_date="2026-01-31"
        )
        self.organization1 = Organization.objects.create(
            name="Factory",
        contact=self.contact,
        products=self.product
        )

        self.organization2 = Organization.objects.create(
            name="Company",
            contact=self.contact,
            products=self.product,
            supplier=self.organization1,
            debt_to_supplier=10000
        )
        self.client.force_authenticate(user=self.user)


    def test_organization1_retrieve(self):
        url = reverse("electronics:org_retrieve", args=[self.organization1.id])  # Используйте имя URL, сгенерированное router
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.organization1.name)

    def test_contact_create(self):
        url = reverse("electronics:contacts-list")
        data = {
            "email": "911@mail.ru",
            "country": "Россия",
            "city": "Дюртюли",
            "street": "Ленина",
            "house_number": 40
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.all().count(), 2)

    def test_contact_update(self):
        url = reverse("electronics:contacts-detail", args=(self.contact.id,))
        data = {
            "city": "Уфа",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("city"), "Уфа")

    def test_contact_delete(self):
        url = reverse("electronics:contacts-detail", args=(self.contact.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contact.objects.all().count(), 0)

    def test_contact_list(self):
        url = reverse("electronics:contacts-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        result = [
    {
        "id": 1,
        "email": "hrustam911@mail.ru",
        "country": "Россия",
        "city": "Дюртюли",
        "street": "Ленина",
        "house_number": "40"
    }]
        self.assertEqual(data, result)