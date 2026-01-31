from django.urls import include, path
from rest_framework import routers


from .views import ContactViewSet, ProductViewSet, OrganizationCreate, OrganizationUpdate, OrganizationRetrieve, \
    OrganizationDestroy, OrganizationList
from users.apps import UsersConfig

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('organizations/create/', OrganizationCreate.as_view(), name='org_create'),
    path('organizations/update/<int:pk>/', OrganizationUpdate.as_view(), name='org_update'),
    path('organizations/retrieve/<int:pk>/', OrganizationRetrieve.as_view(), name='org_retrieve'),
    path('organizations/delete/<int:pk>/', OrganizationDestroy.as_view(), name='org_delete'),
    path('organizations/', OrganizationList.as_view(), name='org_list'),
]