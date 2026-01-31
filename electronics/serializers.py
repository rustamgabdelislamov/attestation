from rest_framework import serializers
from .models import Contact, Product, Organization


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Organization
        fields = ['name', 'contact', 'supplier', 'products', 'debt_to_supplier']


class OrganizationUpdateSerializer(serializers.ModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)  # делаем поле доступным только для чтения

    def validate(self, attrs):
        if 'debt_to_supplier' in self.initial_data:
            raise serializers.ValidationError({'debt_to_supplier': ["Обновление этого поля запрещено"]})
        return attrs