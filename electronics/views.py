from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import Contact, Product, Organization
from .serializers import ContactSerializer, ProductSerializer, OrganizationSerializer, OrganizationUpdateSerializer
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import ValidationError



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrganizationList(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("contact__country",)
    ordering_fields = ("email",)


class OrganizationCreate(generics.CreateAPIView):
    serializer_class = OrganizationSerializer


class OrganizationUpdate(generics.UpdateAPIView):
    serializer_class = OrganizationUpdateSerializer
    queryset = Organization.objects.all()


class OrganizationRetrieve(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDestroy(generics.DestroyAPIView):
    queryset = Organization.objects.all()











